# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-26 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_account', models.CharField(help_text='\u64cd\u4f5c\u5458\u8d26\u53f7', max_length=20, null=True, verbose_name='\u64cd\u4f5c\u5458\u8d26\u53f7')),
                ('record_time', models.DateTimeField(blank=True, help_text='\u8bb0\u5f55\u65f6\u95f4', null=True, verbose_name='\u8bb0\u5f55\u65f6\u95f4')),
                ('device_id', models.CharField(help_text='\u8bbe\u5907ID', max_length=20, verbose_name='\u8bbe\u5907ID')),
                ('sim_id', models.CharField(default='', help_text='SIM ID', max_length=20, verbose_name='SIM ID')),
                ('car_identification_num', models.CharField(blank=True, help_text='\u8f66\u8f86\u8bc6\u522b\u7801', max_length=30, verbose_name='\u8f66\u8f86\u8bc6\u522b\u7801')),
                ('bargain_num', models.CharField(blank=True, help_text='\u51fa\u8ba9\u5408\u540c\u7f16\u53f7', max_length=30, verbose_name='\u51fa\u8ba9\u5408\u540c\u7f16\u53f7')),
                ('remarks', models.TextField(blank=True, help_text='\u5907\u6ce8', verbose_name='\u5907\u6ce8')),
                ('transport_type', models.CharField(choices=[('unknown', '\u672a\u9009\u62e9'), ('send_off', '\u603b\u5e93\u5bc4\u51fa'), ('send_back', '\u7ecf\u9500\u5546\u5bc4\u56de'), ('sell', '\u51fa\u8ba9')], default='unknown', help_text='\u5728\u9014\u7c7b\u578b', max_length=15, verbose_name='\u5728\u9014\u7c7b\u578b')),
                ('record_type', models.CharField(choices=[('unknown', '\u672a\u9009\u62e9'), ('depot_out', '\u5165\u5e93\u8bb0\u5f55'), ('depot_in', '\u5165\u5e93\u8bb0\u5f55'), ('send_back', '\u5bc4\u56de\u8bb0\u5f55'), ('sell', '\u51fa\u8ba9\u8bb0\u5f55'), ('binding', '\u7ed1\u5b9a\u8bb0\u5f55'), ('unbinding', '\u89e3\u7ed1\u8bb0\u5f55')], default='unknown', help_text='\u8bb0\u5f55\u7c7b\u578b', max_length=20, verbose_name='\u8bb0\u5f55\u7c7b\u578b')),
                ('main_factory_name', models.CharField(blank=True, help_text='\u6240\u5c5e\u4e3b\u673a\u5382', max_length=50, verbose_name='\u6240\u5c5e\u4e3b\u673a\u5382')),
                ('division_name', models.CharField(blank=True, help_text='\u6240\u5c5e\u4e8b\u4e1a\u90e8', max_length=50, verbose_name='\u6240\u5c5e\u4e8b\u4e1a\u90e8')),
                ('commercial_name', models.CharField(blank=True, help_text='\u6240\u5c5e\u5546\u52a1\u5904', max_length=50, verbose_name='\u6240\u5c5e\u5546\u52a1\u5904')),
                ('dealer_name', models.CharField(blank=True, help_text='\u7ecf\u9500\u5546', max_length=50, verbose_name='\u7ecf\u9500\u5546')),
                ('dealer_phone', models.CharField(blank=True, help_text='\u7ecf\u9500\u5546\u8054\u7cfb\u65b9\u5f0f', max_length=15, verbose_name='\u7ecf\u9500\u5546\u8054\u7cfb\u65b9\u5f0f')),
            ],
            options={
                'ordering': ['-record_time'],
                'verbose_name': '\u8bbe\u5907\u8bb0\u5f55',
                'verbose_name_plural': '\u8bbe\u5907\u8bb0\u5f55',
            },
        ),
    ]
