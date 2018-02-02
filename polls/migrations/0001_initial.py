# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-26 03:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.CharField(choices=[('unknown', '\u672a\u9009\u62e9'), ('depot_out', '\u51fa\u5e93'), ('depot_in', '\u5165\u5e93'), ('send_back', '\u5bc4\u56de'), ('sell', '\u51fa\u8ba9'), ('binding', '\u7ed1\u5b9a'), ('unbinding', '\u89e3\u7ed1')], default='unknown', help_text='\u6700\u8fd1\u64cd\u4f5c', max_length=10, verbose_name='\u6700\u8fd1\u64cd\u4f5c')),
                ('operation_time', models.DateTimeField(blank=True, help_text='\u6700\u8fd1\u64cd\u4f5c\u65f6\u95f4', null=True, verbose_name='\u6700\u8fd1\u64cd\u4f5c\u65f6\u95f4')),
                ('activate_time', models.DateTimeField(blank=True, help_text='\u6fc0\u6d3b\u65f6\u95f4', null=True, verbose_name='\u6fc0\u6d3b\u65f6\u95f4')),
                ('device_id', models.CharField(help_text='\u8bbe\u5907ID', max_length=20, unique=True, verbose_name='\u8bbe\u5907ID')),
                ('sim_id', models.CharField(help_text='\u8bbe\u5907SIM ID', max_length=20, unique=True, verbose_name='\u8bbe\u5907SIM ID')),
                ('icc_id', models.CharField(help_text='\u8bbe\u5907ICC ID', max_length=20, null=True, unique=True, verbose_name='\u8bbe\u5907ICC ID')),
                ('depot_name', models.CharField(blank=True, help_text='\u8bbe\u5907\u5e93\u623f\u540d\u79f0', max_length=20, verbose_name='\u8bbe\u5907\u5e93\u623f\u540d\u79f0')),
                ('monitor_duration', models.DurationField(default=datetime.timedelta(0), help_text='\u76d1\u63a7\u7d2f\u8ba1\u65f6\u957f', verbose_name='\u76d1\u63a7\u7d2f\u8ba1\u65f6\u957f')),
                ('is_destory', models.BooleanField(default=False, help_text='\u662f\u5426\u5df2\u9500\u6bc1', verbose_name='\u662f\u5426\u5df2\u9500\u6bc1')),
                ('device_init_time', models.DateTimeField(auto_now_add=True, help_text='\u521d\u6b21\u5165\u5e93\u65f6\u95f4', verbose_name='\u521d\u6b21\u5165\u5e93\u65f6\u95f4')),
                ('destory_time', models.DateTimeField(blank=True, help_text='\u9500\u6bc1\u65f6\u95f4', null=True, verbose_name='\u9500\u6bc1\u65f6\u95f4')),
                ('binding_time', models.DateTimeField(blank=True, help_text='\u7ed1\u5b9a\u65f6\u95f4', null=True, verbose_name='\u7ed1\u5b9a\u65f6\u95f4')),
                ('remove_binding_time', models.DateTimeField(blank=True, help_text='\u89e3\u7ed1\u65f6\u95f4', null=True, verbose_name='\u89e3\u7ed1\u65f6\u95f4')),
                ('sell_time', models.DateTimeField(blank=True, help_text='\u51fa\u8ba9\u65f6\u95f4', null=True, verbose_name='\u51fa\u8ba9\u65f6\u95f4')),
                ('send_back_time', models.DateTimeField(blank=True, help_text='\u5bc4\u56de\u65f6\u95f4', null=True, verbose_name='\u5bc4\u56de\u65f6\u95f4')),
                ('depot_in_time', models.DateTimeField(blank=True, help_text='\u5165\u5e93\u65f6\u95f4', null=True, verbose_name='\u5165\u5e93\u65f6\u95f4')),
                ('depot_out_time', models.DateTimeField(blank=True, help_text='\u51fa\u5e93\u65f6\u95f4', null=True, verbose_name='\u51fa\u5e93\u65f6\u95f4')),
                ('device_position', models.CharField(choices=[('enroute', '\u5728\u9014'), ('main_depot', '\u603b\u5e93'), ('dealer_depot', '\u7ecf\u9500\u5546\u5e93\u5b58'), ('major_depot', '\u5927\u5ba2\u6237\u5e93\u5b58')], default='main_depot', help_text='\u6240\u5728\u4f4d\u7f6e\u7c7b\u578b', max_length=20, verbose_name='\u6240\u5728\u4f4d\u7f6e\u7c7b\u578b')),
                ('binding_status', models.CharField(choices=[('binding', '\u5df2\u7ed1\u5b9a'), ('unbinding', '\u672a\u7ed1\u5b9a')], default='unbinding', help_text='\u7ed1\u5b9a\u72b6\u6001', max_length=15, verbose_name='\u7ed1\u5b9a\u72b6\u6001')),
                ('device_ownership', models.CharField(choices=[('main', '\u603b\u5e93'), ('dealer', '\u7ecf\u9500\u5546'), ('major', '\u5927\u5ba2\u6237')], default='main', help_text='\u6240\u5c5e\u6743\u5f52\u5c5e\u72b6\u6001', max_length=20, verbose_name='\u6240\u5c5e\u6743\u5f52\u5c5e\u72b6\u6001')),
                ('minotor_status', models.CharField(choices=[('not_monitoring', '\u672a\u76d1\u63a7'), ('monitoring', '\u76d1\u63a7\u4e2d')], default='not_monitoring', help_text='\u76d1\u63a7\u72b6\u6001', max_length=15, verbose_name='\u76d1\u63a7\u72b6\u6001')),
                ('is_new_device', models.BooleanField(default=True, help_text='\u662f\u5426\u4e3a\u65b0\u8bbe\u5907', verbose_name='\u662f\u5426\u4e3a\u65b0\u8bbe\u5907')),
                ('operator_account', models.CharField(help_text='\u64cd\u4f5c\u5458\u8d26\u53f7', max_length=20, null=True, verbose_name='\u64cd\u4f5c\u5458\u8d26\u53f7')),
                ('car_identification_num', models.CharField(blank=True, help_text='\u8f66\u8f86\u8bc6\u522b\u7801', max_length=30, verbose_name='\u8f66\u8f86\u8bc6\u522b\u7801')),
            ],
        ),
    ]