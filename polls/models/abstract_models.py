#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class BaseModel(models.Model):
  create_time = models.DateTimeField(
    u'创建时间',
    auto_now_add=True,
    blank=True,
    null=True,
    help_text=u'创建时间',
  )
  update_time = models.DateTimeField(
    u'更新时间',
    auto_now=True,
    blank=True,
    null=True,
    help_text=u'更新时间',
  )

  @property
  def self(self):
    return self

  class Meta:
    abstract = True

class DeletedMixin(models.Model):
  deleted = models.BooleanField(
    u'是否已删除',
    default=False,
    blank=True,
    help_text=u'是否已删除',
  )

  class Meta:
    abstract = True

class LocationMixin(models.Model):
  lat = models.FloatField(
    u'纬度',
    blank=True,
    null=True,
    help_text=u'纬度',
  )
  lng = models.FloatField(
    u'经度',
    blank=True,
    null=True,
    help_text=u'经度',
  )
  address = models.CharField(
    u'定位地址',
    max_length=80,
    default='',
    blank=True,
    help_text=u'定位地址',
  )

  class Meta:
    abstract = True

class ContactMixin(models.Model):
  contact_name = models.CharField(
    u'联系人',
    max_length=50,
    default='',
    blank=True,
    help_text=u'联系人',
  )
  contact_phone = models.CharField(
    u'联系电话',
    max_length=20,
    default='',
    blank=True,
    help_text=u'联系电话',
  )

  class Meta:
    abstract = True

class BatteryMixin(models.Model):
  battery_code = models.CharField(
    u'电池系统编码',
    max_length=50,
    null=True,
    help_text=u'电池系统编码',
  )
  battery_manufacturer = models.CharField(
    u'电池制造商',
    max_length=3,
    null=True,
    help_text=u'电池制造商',
  )
  battery_type = models.CharField(
    u'电池型号',
    max_length=30,
    null=True,
    help_text=u'电池型号',
  )
  battery_capacity = models.FloatField(
    u'电池电量',
    null=True,
    help_text=u'电池电量'
  )
  battery_cooling_way = models.CharField(
    u'电池冷却方式',
    max_length=50,
    null=True,
    help_text=u'电池冷却方式',
  )

  class Meta:
    abstract = True

class MotorMixin(models.Model):
  motor_type = models.CharField(
    u'驱动电机型号',
    max_length=30,
    null=True,
    help_text=u'驱动电机型号',
  )
  motor_serial_num = models.CharField(
    u'电机序号',
    max_length=60,
    null=True,
    help_text=u'电机序号',
  )
  motor_cooling_way = models.CharField(
    u'电机冷却方式',
    max_length=50,
    null=True,
    help_text=u'电机冷却方式',
  )
  motor_nominal_voltage = models.CharField(
    u'电机额定电压',
    null=True,
    help_text=u'电机额定电压',
  )
  motor_max_electricity = models.FloatField(
    u'电机最大工作流',
    null=True,
    help_text=u'电机最大工作流',
  )
  motor_max_power = models.FloatField(
    u'电机峰值功率',
    null=True,
    help_text=u'电机峰值功率',
  )
  motor_max_rotating_speed = models.FloatField(
    u'电机最高转速',
    null=True,
    help_text=u'电机最高转速',
  )
  motor_max_torque = models.FloatField(
    u'电机峰值转矩',
    null=True,
    help_text=u'电机峰值转矩',
  )
  motor_output_torque = models.FloatField(
    u'电机输出转矩',
    null=True,
    help_text=u'电机输出转矩',
  )

  class Meta:
    abstract = True

class EagleMixin(models.Model):
  eagle_entity_name = models.CharField(
    u'鹰眼实体',
    max_length=50,
    default='',
    blank=True,
    help_text=u'鹰眼实体',
  )
  has_eagle_entity = models.BooleanField(
    u'是否创建了实例',
    default=False,
    blank=True,
    help_text=u'是否创建了实例',
  )

  class Meta:
    abstract = True

class MonitorSwitchMixin(models.Model):
    voltage_lt = models.BooleanField(
        u'电压过低',
        default=True,
        blank=True,
        help_text=u'电压过低',
    )
    unable_locate_gt = models.BooleanField(
        u'无法定位',
        default=True,
        blank=True,
    )
    device_offline = models.BooleanField(
        u'设备离线',
        default=True,
        blank=True,
    )
    check_mileage = models.BooleanField(
        u'运营里程',
        default=True,
        blank=True,
    )
    park_timeout = models.BooleanField(
        u'超时停车',
        default=True,
        blank=True,
    )
    night_running_end = models.BooleanField(
        u'夜间行驶',
        default=True,
        blank=True,
    )
    fatigue_driving_gt = models.BooleanField(
        u'疲劳驾驶',
        default=True,
        blank=True,
    )
    overspeed_gt = models.BooleanField(
        u'超速',
        default=True,
        blank=True,
    )
    over_region = models.BooleanField(
        u'超越区域',
        default=True,
        blank=True,
    )
    temperature_difference = models.BooleanField(
        u'温度差异',
        default=True,
        blank=True,
    )
    electrode_gt = models.BooleanField(
        u'电池极柱高温',
        default=True,
        blank=True,
    )
    battery_pressure_gt = models.BooleanField(
        u'电池包过压',
        default=True,
        blank=True,
    )
    battery_pressure_lt = models.BooleanField(
        u'电池包过压',
        default=True,
        blank=True,
    )
    soc_lt = models.BooleanField(
        u'soc低',
        default=True,
        blank=True,
    )
    soc_too_lt = models.BooleanField(
        u'soc过低',
        default=True,
        blank=True,
    )
    soc_gt = models.BooleanField(
        u'soc过高',
        default=True,
        blank=True,
    )
    single_battery_pressure_lt = models.BooleanField(
        u'单体蓄电池欠压',
        default=True,
        blank=True,
    )
    single_battery_pressure_gt = models.BooleanField(
        u'单体蓄电池过压',
        default=True,
        blank=True,
    )
    motor_battery_unmatch = models.BooleanField(
        u'动力蓄电池不匹配',
        default=True,
        blank=True,
    )
    motor_battery_consistency_bad = models.BooleanField(
        u'动力蓄电池一致性差',
        default=True,
        blank=True,
    )
    motor_battery_consistency_bad = models.BooleanField(
        u'动力蓄电池一致性差',
        default=True,
        blank=True,
    )
    isolation_fault = models.BooleanField(
        u'绝缘故障',
        default=True,
        blank=True,
    )
    dc_temperature = models.BooleanField(
        u'DC温度',
        default=True,
        blank=True,
    )
    dc_status = models.BooleanField(
        u'DC状态',
        default=True,
        blank=True,
    )
    break_system = models.BooleanField(
        u'制动系统',
        default=True,
        blank=True,
    )
    motor_controller_temperature = models.BooleanField(
        u'电机控制器温度',
        default=True,
        blank=True,
    )
    high_pressure_lock = models.BooleanField(
        u'高压互锁',
        default=True,
        blank=True,
    )
    electric_motor_temperature = models.BooleanField(
        u'驱动电机温度',
        default=True,
        blank=True,
    )
    storage_system_fault = models.BooleanField(
        u'储能系统故障',
        default=True,
        blank=True,
    )

    class Meta:
        abstract = True


class ElectricMonitorValueMixin(models.Model):
    soc_lt = models.FloatField(
        u'soc低于',
        blank=True,
        default=True,
    )
    soc_too_lt = models.FloatField(
        u'soc太低',
        blank=True,
        default=True,
    )
    soc_gt = models.FloatField(
        u'soc高于',
        blank=True,
        default=True,
    )
    temperature_difference = models.FloatField(
        u'温度差异',
        blank=True,
        default=True,
    )
    dc_gt = models.FloatField(
        u'dc-dc温度高于',
        blank=True,
        default=True,
    )
    electrode_gt = models.FloatField(
        u'电池极柱温度高于',
        blank=True,
        default=True,
    )
    battery_pressure_gt = models.FloatField(
        u'电池包压力大于',
        blank=True,
        default=True,
    )
    battery_pressure_lt = models.FloatField(
        u'电池包压力小于',
        blank=True,
        default=True,
    )
    electric_motor_temperature_gt = models.FloatField(
        u'驱动电机温度高于',
        blank=True,
        default=True,
    )
    electric_motor_temperature_lt = models.FloatField(
        u'驱动电机温度低于',
        blank=True,
        default=True,
    )
    electric_controller_temperature_gt = models.FloatField(
        u'电机控制器温度高于',
        blank=True,
        default=True,
    )
    electric_controller_temperature_lt = models.FloatField(
        u'电机控制器温度低于',
        blank=True,
        default=True,
    )
    storage_pressure_gt = models.FloatField(
        u'车载储存压力高于',
        blank=True,
        default=True,
    )
    storage_pressure_lt = models.FloatField(
        u'车载储存压力低于',
        blank=True,
        default=True,
    )

    class Meta:
        abstract = True
