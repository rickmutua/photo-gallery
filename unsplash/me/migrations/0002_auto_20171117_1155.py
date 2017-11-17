# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='me.Editor')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='me.Tags'),
        ),
    ]
