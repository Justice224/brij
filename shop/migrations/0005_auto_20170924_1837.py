# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_userprofile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='number',
            field=models.CharField(max_length=20),
        ),
    ]
