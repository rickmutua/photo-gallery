# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0002_auto_20171117_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='post/'),
            preserve_default=False,
        ),
    ]
