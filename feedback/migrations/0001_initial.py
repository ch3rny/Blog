# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 10:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=75, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Содержимое')),
                ('created_time', models.DateTimeField(default=datetime.datetime(2017, 7, 30, 10, 49, 28, 590178, tzinfo=utc))),
                ('attachment', models.FileField(upload_to='reviews')),
                ('unread', models.BooleanField(default=True)),
            ],
        ),
    ]
