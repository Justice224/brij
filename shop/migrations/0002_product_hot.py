# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hot',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=20),
            preserve_default=False,
        ),
    ]
