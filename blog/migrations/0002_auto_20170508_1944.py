# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 16:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='count',
            new_name='numbirs',
        ),
    ]