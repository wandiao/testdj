#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from polls import models

class DeviceSerializer(serializers.ModelSerializer):
  holder_name = serializers.CharField(
    source='holder.name',
    read_only=True
  )
  owner_name = serializers.CharField(
    source='owner.name',
    read_only=True,
  )
  client_owner_name = serializers.CharField(
    source='client_owner.name',
    read_only=True,
  )
  supplier_name = serializers.CharField(
    source='supplier.name',
    read_only=True,
  )
  
  class Meta:
    model = models.Device
    read_only_fields = (
      'destroy_time',
      'binding_time',
      'sell_time',
      'send_back_time',
      'depot_out_time',
      'device_using_time',
      'remove_binding_time',
      'holder_name',
      'owner_name',
      'client_owner_name',
      'supplier_name',
      'operation_type',
      'operation_time',
      'monitor_time',
      'is_destroyed',
      'device_init_time',
    )
    fields = read_only_fields + (
      'id',
      'device_id',
      'sim_id',
      'icc_id',
      'supplier',
      'car_identification_num',
      'activate_time',
      'depot_name',
      'device_position',
      'binding_status',
      'device_ownership',
      'monitor_status',
      'is_new_device',
      'operator_account',
      'owner',
      'holder',
      'depot',
      'client_owner',
      'depot_in_time',
    )

class DeviceCreateSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.Device
    fields = (
      'id',
      'device_id',
      'sim_id',
      'depot',
      'depot_name',
      'operator_account',
      'icc_id',
      'supplier',
    )

class DeviceUpdateSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.Device
    fields = (
      'depot_name',
      'destory_name',
      'binding_time',
      'remove_binding_time',
      'sell_time',
      'send_back_time',
      'depot_in_time',
      'depot_out_time',
      'device_position',
      'binding_status',
      'device_ownership',
      'monitor_status',
      'is_new_device',
      'owner',
      'holder',
      'car_identification_num',
      'operator_account',
      'client_owner',
      'activate_time',
      'operation_time',
      'operation_type',
      'monitor_duration',
    )

class ProfileSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Profile
    fields = (
      'id',
      'user',
      'phone',
      'name',
      'role',
      'rank',
      'phone_verified',
    )

ProfileDetailSerializer = ProfileSerializer

class DeviceRecordSerializer(serializers.ModelSerializer):
  binding_status = serializers.CharField(
    source='device.binding_status',
    read_only=True,
  )
  device_position = serializers.CharField(
    source='device.device_position',
    read_only=True,
  )
  device_ownership = serializers.CharField(
    source='device.device_ownership',
    read_only=True,
  )
  monitor_status = serializers.CharField(
    source='device.monitor_status',
    read_only=True,
  )
  device_using_time = serializers.CharField(
    source='device.device_using_time',
    read_only=True,
  )
  supplier = serializers.CharField(
    source='device.supplier.name',
    read_only=True,
  )
  depot_name = serializers.CharField(
    source='device.depot_name',
    read_only=True,
  )
  record_type_display = serializers.SerializerMethodField()
  transport_type_display = serializers.SerializerMethodField()
  is_new_device = serializers.SerializerMethodField()

  class Meta:
    model = models.DeviceRecord
    fields = (
      'id',
      'record_type',
      'record_type_display',
      'transport_type',
      'transport_type_display',
      'is_new_device',
      'record_time',
      'device_id',
      'sim_id',
      'car_identification_num',
      'bargain_num',
      'operator_account',
      'remarks',
      'supplier',
      'depot_name',
      'binding_status',
      'monitor_status',
      'device_position',
      'device_ownership',
      'device_using_time',
      'main_factory_name',
      'division_name',
      'commercial_name',
      'dealer_name',
      'dealer_phone',
    )

  def get_record_type_display(self, obj):
    return obj.get_record_type_display()
  
  def get_transport_type_display(self, obj):
    return obj.get_transport_type_display()
  
  def get_is_new_device(self, obj):
    return models.Device.objects.get(device_id=obj.device_id).is_new_device


class IDInfoSerializer(serializers.Serializer):
  device_id = serializers.CharField(
    max_length=20,
    help_text=u'设备ID',
  )
  sim_id = serializers.CharField(
    max_length=20,
    help_text=u'设备SIM ID',
  )
  icc_id = serializers.CharField(
    max_length=20,
    help_text=u'设备icc ID',
  )

class DepotInSerializer(serializers.Serializer):
  id_info_list = IDInfoSerializer(
    many=True,
    help_text=u'新设备入库信息列表',
    required=False,
  )
  device_ids = serializers.ListField(
    child=serializers.CharField(),
    help_text=u'入库设备ID列表',
    required=False,
  )
  remarks = serializers.CharField(
    required=False,
    default='',
    help_text=u'备注',
  )
  supplier = serializers.CharField(
    help_text=u'设备供应商',
    required=False,
  )
  depot = serializers.CharField(
    help_text=u'库房',
  )
  
