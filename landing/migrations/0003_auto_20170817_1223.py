# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20170815_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'My Subscriber', 'verbose_name_plural': 'A lot of Subscribers'},
        ),
    ]
