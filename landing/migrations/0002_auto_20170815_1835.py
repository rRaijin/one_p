# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Subscriber',
        ),
    ]
