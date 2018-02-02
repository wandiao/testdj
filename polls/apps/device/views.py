# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import (
  viewsets,
)

from polls.common import serializers as common_serializers

from django.shortcuts import render
from polls.models import Device

def testView(request):
  context = {}
  context['devices'] =  Device.objects.all()
  return render(request, 'polls/test.html', context)


class DeviceViewSet(viewsets.ModelViewSet):
  
  queryset = Device.objects.filter(is_destroyed=False)
  serializer_class = common_serializers.DeviceSerializer
  lookup_field = 'device_id'
