# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-28 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_complaint_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tid',
            name='id',
        ),
        migrations.AlterField(
            model_name='tid',
            name='flat_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
