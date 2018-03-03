# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db.models import Q
from django.db.transaction import atomic
from rest_framework import (
  viewsets,
  status,
  serializers as rest_serializers,
)

from polls.common import serializers as common_serializers
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from django.shortcuts import render
from polls import models

def testView(request):
  context = {}
  context['devices'] =  Device.objects.all()
  return render(request, 'polls/test.html', context)


class DeviceViewSet(viewsets.ModelViewSet):

  queryset = models.Device.objects.filter(is_destroyed=False)
  serializer_class = common_serializers.DeviceSerializer
  lookup_field = 'device_id'
  filter_fields = (
    'supplier',
    'depot_name',
    'depot',
    'holder',
    'device_position',
    'binding_status',
    'monitor_status',
    'is_destroyed',
    'operation_type',
  )
  search_fields = ('device_id', 'sim_id', 'operator_account')

  def get_queryset(self):
    queryset = self.queryset
    operator = self.request.user.profile
    content_object = operator.content_object
    device_positions = self.request.GET.get('device_positions', '')
    if operator.role == 'super_admin' and operator.rank == 'platform_company':
      queryset = models.Device.objects.all()
    elif isinstance(content_object, models.Client):
      queryset = queryset.filter(client_owner=content_object.id)
    elif isinstance(content_object, models.Dealer):
      queryset = queryset.filter(
        Q(holder=content_object.id) | Q(owner=content_object.id)
      )
    else:
      queryset = queryset.filter(
        Q(device_ownership='main') | Q(device_ownership='major')
      )
    using_year = self.request.query_params.get('using_year', None)
    if using_year is not None:
      now = datetime.datetime.now()
      eariler_time = now - datetime.timedelta(days=int(using_year) * 365)
      queryset = queryset.filter(device_init_time__lt=eariler_time)
    if device_positions:
      device_positions = device_positions.split(',')
      res = models.Device.objects.none()
      for position in device_position:
        res = res | queryset.filter(device_position=position)
      queryset = res
    return queryset.order_by('depot_in_time')
  def get_serializer_class(self):
    if self.action == 'multi_depot_in':
      return common_serializers.DepotInSerializer
    else:
      return common_serializers.DeviceSerializer
  
  @list_route(methods=['post'])
  @atomic
  def multi_depot_in(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    depot_in_time = datetime.datetime.now()
    if serializer.is_valid():
      keys = serializer.data.keys()
      operator = self.request.user.profile
      remarks = serializer.data['remarks']
      depot = serializer.data['depot']
      if 'device_id' not in keys and 'id_info_list' not in keys:
        raise rest_serializers.ValidationError({
          'error': u'没有指定入库设备信息',
        })
      try:
        depot = models.Depot.objects.get(name=depot)
      except models.Depot.DoesNotExist:
        raise rest_serializers.ValidationError({
          'error': u'库房不存在',
        })
      if 'id_info_list' in keys:
        try:
          supplier = serializer.data['supplier']
          supplier = models.Supplier.objects.get(name=supplier)
        except KeyError:
          raise rest_serializers.ValidationError({
            'error': u'没有为新设备指定供应商',
          })
        except models.Supplier.DoesNotExist:
          raise rest_serializers.ValidationError({
            'error': u'供应商不存在',
          })
        if serializer.data['id_info_list']:
          id_infos = serializer.data['id_info_list']
          for id_info in id_infos:
            data = dict(
              operation_type='depot_in',
              operation_time=depot_in_time,
              device_id=id_info['device_id'],
              sim_id=id_info['sim_id'],
              icc_id=id_info['icc_id'],
              operator_acconut=operator.phone,
              supplier=supplier.id,
              depot_in_time=depot_in_time,
              depot=depot.id,
              depot_name=depot.name,
            )
            device_serializer = common_serializers.DeviceSerializer(data=data)
            if device_serializer.is_valid():
              self.perform_create(device_serializer)
            else:
              return Response(device_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            record_data = dict(
              record_type='depot_in',
              record_time=depot_in_time,
              device_id=id_info['device_id'],
              sim_id=id_info['sim_id'],
              operator_account=operator.phone,
              remarks=remarks,
            )
            device_record = common_serializers.DeviceRecordSerializer(data=record_data)
            if device_record.is_valid():
              device_record.save()
            else:
              return Response(device_record.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
          raise rest_serializers.ValidationError({
            'error': u'新设备入库信息列表无效',
          })
      if 'device_ids' in keys:
        if serializer.data['device_ids']:
          content_object = operator.content_object
          if isinstance(content_object, models.Dealer):
            device_position = 'dealer_depot'
            holder = content_object.id
          else:
            device_position = 'main_depot'
            holder = None
          device_ids = serializer.data['device_ids']
          for device_id in device_ids:
            instance = models.Device.objects.get(device_id=device_id)
            device_serializer = common_serializers.DeviceUpdateSerializer(
              instance,
              data={
                'operation_type': 'depot_in',
                'operation_time': depot_in_time,
                'operation_account': operator.phone,
                'depot_in_time': depot_in_time,
                'device_position': device_position,
                'depot': depot_id,
                'depot_name': depot.name,
                'holder': holder,
              },
              partial=True,
            )
            if device_serializer.is_valid():
              self.perform_update(device_serializer)
            else:
              return Response(device_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            record_data = dict(
              record_type='depot_in',
              record_time=depot_in_time,
              device_id=instance.device_id,
              sim_id=instance.sim_id,
              operator_account=operator.phone,
              remarks=remarks,
            )
            device_record = common_serializers.DeviceRecordSerializer(data=record_data)
            if device_record.is_valid():
              device_record.save()
            else:
              return Response(device_record.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
          raise rest_serializers.ValidationError({
            'error': u'入库设备ID列表无效',
          })
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors)


class DeviceRecordViewSet(viewsets.ReadOnlyModelViewSet):

  queryset = models.DeviceRecord.objects.all()
  serializer_class = common_serializers.DeviceRecordSerializer
  filter_fields = ('record_type', 'device_id')
  search_fields = (
    'dealer_name',
    'commercial_name',
    'division_name',
    'main_factory_name',
    'device_id',
    'sim_id',
  )

  def get_queryset(self):
    queryset = self.queryset
    start_time = self.request.query_params.get('start_time', None)
    end_time = self.request.query_params.get('end_time', None)
    record_types = self.request.GET.get('record_types', '')
    if start_time:
      start_time = datetime.datetime.strftime(start_time, '%Y-%m-%d')
      end_time = datetime.datetime.strftime(
        end_time, '%Y-%m-%d') if end_time else datetime.datetime.now()
      queryset = queryset.filter(
        record_time__gte=start_time,
        record_time__lte=end_time,
      )
    if record_types:
      record_types = record_types.split(',')
      res = models.DeviceRecord.objects.none()
      for record_type in record_types:
        res = res | queryset.filter(record_type=record_type)
      queryset = res
    return queryset
  
  def count_sign(self, request, device_id):
    records = self.get_queryset().filter(device_id=device_id)
    data = dict(
      depot_out=records.filter(record_type='depot_out').count(),
      depot_in=records.filter(record_type='depot_in').count(),
      send_back=records.filter(record_type='send_back').count(),
      sell=records.filter(record_type='sell').count(),
      binding=records.filter(record_type='binding').count(),
      unbinding=records.filter(record_type='unbinding').count(),
    )
    return Response(data)

