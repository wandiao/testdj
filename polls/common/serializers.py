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