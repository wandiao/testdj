# coding:utf-8

from __future__ import unicode_literals
import datetime

from django.db import models

from .abstract_models import (
    BaseModel,
)

class Device(models.Model):
  DEVICE_POSITION_CHOIES = (
    ('enroute', u'在途'),
    ('main_depot', u'总库'),
    ('dealer_depot', u'经销商库存'),
    ('major_depot', u'大客户库存'),
  )
  BINDING_STATUS_CHOICES = (
      ('binding', u'已绑定'),
      ('unbinding', u'未绑定'),
    )
  DEVICE_OWNER_CHOICES = (
    ('main', u'总库'),
    ('dealer', u'经销商'),
    ('major', u'大客户'),
  )
  MONITOR_STATUS_CHOICES = (
    ('not_monitoring', u'未监控'),
    ('monitoring', u'监控中'),
  )
  OPERATION_TYPE = (
    ('unknown', u'未选择'),
    ('depot_out', u'出库'),
    ('depot_in', u'入库'),
    ('send_back', u'寄回'),
    ('sell', u'出让'),
    ('binding', u'绑定'),
    ('unbinding', u'解绑'),
  )

  operation_type = models.CharField(
    u'最近操作',
    max_length=10,
    choices=OPERATION_TYPE,
    default='unknown',
    help_text=u'最近操作',
  )
  operation_time = models.DateTimeField(
    u'最近操作时间',
    blank=True,
    null=True,
    help_text=u'最近操作时间',
  )
  activate_time = models.DateTimeField(
    u'激活时间',
    blank=True,
    null=True,
    help_text=u'激活时间'
  )
  supplier = models.ForeignKey(
    'polls.Supplier',
    verbose_name=u'设备供应商',
    null=True,
    blank=True,
    on_delete=models.PROTECT,
    help_text=u'设备供应商',
  )
  device_id = models.CharField(
    u'设备ID',
    max_length=20,
    null=False,
    unique=True,
    help_text=u'设备ID',
  )
  sim_id = models.CharField(
    u'设备SIM ID',
    max_length=20,
    unique=True,
    help_text=u'设备SIM ID',
  )
  icc_id = models.CharField(
    u'设备ICC ID',
    max_length=20,
    null=True,
    unique=True,
    help_text=u'设备ICC ID',
  )
  depot = models.ForeignKey(
    'polls.Depot',
    verbose_name=u'库房',
    blank=True,
    null=True,
    on_delete=models.PROTECT,
    help_text=u'库房',
  )
  depot_name = models.CharField(
    u'设备库房名称',
    max_length=20,
    blank=True,
    help_text=u'设备库房名称',
  )
  monitor_duration = models.DurationField(
    u'监控累计时长',
    default=datetime.timedelta(0),
    help_text=u'监控累计时长',
  )
  is_destroyed = models.BooleanField(
    u'是否已销毁',
    default=False,
    help_text=u'是否已销毁',
  )
  device_init_time = models.DateTimeField(
    u'初次入库时间',
    auto_now_add=True,
    help_text=u'初次入库时间',
  )
  destroy_time = models.DateTimeField(
    u'销毁时间',
    blank=True,
    null=True,
    help_text=u'销毁时间',
  )
  binding_time = models.DateTimeField(
    u'绑定时间',
    blank=True,
    null=True,
    help_text=u'绑定时间',
  )
  remove_binding_time = models.DateTimeField(
    u'解绑时间',
    blank=True,
    null=True,
    help_text=u'解绑时间'
  )
  sell_time = models.DateTimeField(
    u'出让时间',
    blank=True,
    null=True,
    help_text=u'出让时间',
  )
  send_back_time = models.DateTimeField(
    u'寄回时间',
    blank=True,
    null=True,
    help_text=u'寄回时间',
  )
  depot_in_time = models.DateTimeField(
    u'入库时间',
    blank=True,
    null=True,
    help_text=u'入库时间',
  )
  depot_out_time = models.DateTimeField(
    u'出库时间',
    blank=True,
    null=True,
    help_text=u'出库时间',
  )
  device_position = models.CharField(
    u'所在位置类型',
    default='main_depot',
    max_length=20,
    choices=DEVICE_POSITION_CHOIES,
    help_text=u'所在位置类型',
  )
  binding_status = models.CharField(
    u'绑定状态',
    default='unbinding',
    max_length=15,
    choices=BINDING_STATUS_CHOICES,
    help_text=u'绑定状态',
  )
  device_ownership = models.CharField(
    u'所属权归属状态',
    default='main',
    max_length=20,
    choices=DEVICE_OWNER_CHOICES,
    help_text=u'所属权归属状态',
  )
  monitor_status = models.CharField(
    u'监控状态',
    default='not_monitoring',
    max_length=15,
    choices=MONITOR_STATUS_CHOICES,
    help_text=u'监控状态',
  )
  is_new_device = models.BooleanField(
    u'是否为新设备',
    default=True,
    help_text=u'是否为新设备',
  )
  owner = models.ForeignKey(
    'polls.Dealer',
    verbose_name = u'所属经销商',
    related_name='own_devices',
    blank=True,
    null=True,
    on_delete=models.PROTECT,
    help_text='所属经销商',
  )
  holder = models.ForeignKey(
    'polls.Dealer',
    verbose_name=u'设备持有者',
    related_name='holde_devices',
    blank=True,
    null=True,
    on_delete=models.PROTECT,
    help_text=u'设备持有者',
  )
  client_owner = models.ForeignKey(
    'polls.Client',
    verbose_name=u'所属大客户',
    related_name=u'own_devices',
    blank=True,
    null=True,
    on_delete=models.PROTECT,
    help_text=u'所属大客户',
  )
  operator_account = models.CharField(
    u'操作员账号',
    max_length=20,
    null=True,
    help_text=u'操作员账号',
  )
  car_identification_num = models.CharField(
    u'车辆识别码',
    max_length=30,
    blank=True,
    help_text=u'车辆识别码',
  )

  def __unicode__(self):
    return self.device_id

  @property
  def device_using_time(self):
    return datetime.datetime.now() - self.device_init_time

  @property
  def monitor_time(self):
    monitor_duration = self.monitor_duration
    if self.minotor_status == 'monitoring':
      if self.activate_time:
        a_time = self.activate_time
        return datetime.datetime.now() - a_time + monitor_duration
      else:
        b_time = self.binding_time
        return datetime.datetime.now() - b_time + monitor_duration
    else:
      return monitor_duration
  
  class Meta:
    verbose_name = u'设备信息'
    verbose_name_plural = verbose_name

class Supplier(BaseModel):
  name = models.CharField(
    u'设备供应商',
    max_length=50,
    help_text=u'设备供应商',
  )

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'设备供应商'
    verbose_name_plural = verbose_name
