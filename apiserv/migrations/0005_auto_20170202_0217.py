# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiserv', '0004_auto_20170201_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mem_type',
            field=models.IntegerField(choices=[(0, 'UNPAID'), (1, 'PAID'), (2, 'CREDIT')], default=0),
        ),
    ]
