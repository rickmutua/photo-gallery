# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
