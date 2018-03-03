# coding:utf-8

from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRelation,
)

from django.db import models

from .abstract_models import (
    BaseModel,
    DeletedMixin,
    ContactMixin,
)

class PlatformCompany(DeletedMixin, ContactMixin, BaseModel):
  rank = 'platform_company'
  name = models.CharField(
    u'公司名称',
    max_length=50,
    help_text=u'公司名称',
  )

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'总平台公司'
    verbose_name_plural = verbose_name

class MainFactory(DeletedMixin, ContactMixin, BaseModel):
  rank = 'main_factory'
  platform_company = models.ForeignKey(
    'polls.PlatformCompany',
    null=True,
    blank=True,
    on_delete=models.PROTECT,
    verbose_name=u'平台公司',
    help_text=u'平台公司'
  )
  name = models.CharField(
    u'主机厂名称',
    max_length=50,
    help_text=u'主机厂名称',
  )

  def __unicode__(self):
    return self.name
  class Meta:
    verbose_name = u'主机厂'
    verbose_name_plural = verbose_name

class Division(DeletedMixin, ContactMixin, BaseModel):
  rank = 'division'
  main_factory = models.ForeignKey(
    'polls.MainFactory',
    null=True,
    blank=True,
    on_delete=models.PROTECT,
    verbose_name=u'主机厂',
    help_text=u'主机厂',
  )
  name = models.CharField(
    u'事业部名称',
    max_length=50,
    help_text=u'事业部名称',
  )

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'事业部'
    verbose_name_plural = verbose_name

class Commercial(DeletedMixin, ContactMixin, BaseModel):
  rank = 'commercial'
  division = models.ForeignKey(
    'polls.Division',
    null=True,
    blank=True,
    on_delete=models.PROTECT,
    verbose_name=u'事业部',
    help_text=u'事业部',
  )
  name = models.CharField(
    u'商务处名称',
    max_length=50,
    help_text=u'商务处名称',
  )

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'商务处'
    verbose_name_plural = verbose_name

class Dealer(DeletedMixin, ContactMixin, BaseModel):
  rank = 'dealer'
  commercials = models.ManyToManyField(
    'polls.Commercial',
    verbose_name=u'商务处',
    help_text=u'商务处',
  )
  name = models.CharField(
    u'经销商名称',
    max_length=50,
    help_text=u'经销商名称',
  )
  short_name = models.CharField(
    u'经销商简称',
    max_length=50,
    help_text=u'经销商简称',
  )
  dealer_number = models.CharField(
    u'经销商编号',
    max_length=50,
    help_text=u'经销商编号',
  )
  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'经销商'
    verbose_name_plural = verbose_name

class Client(DeletedMixin, ContactMixin, BaseModel):
  rank = 'major'
  name = models.CharField(
    u'客户名称',
    max_length=50,
    null=True,
    help_text=u'客户名称',
  )
  dealers = models.ManyToManyField(
    'polls.Dealer',
    verbose_name=u'经销商',
    help_text=u'经销商',
  )

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'客户'
    verbose_name_plural = verbose_name

class Depot(models.Model):
  DEPOT_TYPE = (
    ('main_depot', u'总库库房'),
    ('dealer_depot', u'经销商库房'),
  )

  depot_type = models.CharField(
    u'库房类型',
    max_length=15,
    choices=DEPOT_TYPE,
    default='main_depot',
    help_text=u'库房类型',
  )
  name = models.CharField(
    u'库房名称',
    max_length=50,
    help_text=u'库房名称',
  )
  dealer = models.ForeignKey(
    'polls.Dealer',
    blank=True,
    null=True,
    verbose_name=u'所属经销商',
    help_text=u'所属经销商',
  )

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'库房'
    verbose_name_plural = verbose_name

class Profile(DeletedMixin, BaseModel):

  RANK_CHOICES = (
    ('platform_company', u'总平台公司'),
    ('main_factory', u'主机厂'),
    ('disivion', u'事业部'),
    ('commercial', u'商务处'),
    ('dealer', u'经销商'),
    ('major', u'大客户'),
  )
  ROLE_CHOICES = (
    ('super_admin', u'超级管理员'),
    ('admin', u'管理员'),
    ('worker', u'业务员'),
    ('warekeeper', u'仓库管理员')
  )
  content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')
  rank = models.CharField(
    u'层级',
    max_length=20,
    choices=RANK_CHOICES,
    help_text=u'层级'
  )
  role = models.CharField(
    u'角色',
    max_length=20,
    choices=ROLE_CHOICES,
    help_text=u'角色',
  )
  user = models.OneToOneField(
    'auth.User',
    verbose_name=u'用户',
    on_delete=models.PROTECT,
    help_text=u'用户',
  )
  phone = models.CharField(
    u'电话',
    max_length=20,
    help_text=u'电话',
  )
  name = models.CharField(
    u'姓名',
    max_length=20,
    help_text=u'姓名'
  )
  phone_verified = models.BooleanField(
    u'电话是否已验证',
    default=False,
    blank=True,
    help_text=u'电话是否已验证',
  )
  depot = models.ForeignKey(
    'polls.depot',
    verbose_name=u'负责仓库',
    blank=True,
    null=True,
    related_name='depot_keepers',
    on_delete=models.PROTECT,
    help_text=u'负责仓库',
  )

  def __unicode__(self):
    return self.name
  
  class Meta:
    verbose_name = u'个人信息'
    verbose_name_plural = verbose_name
