# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-23 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180317_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.IntegerField(default=1),
        ),
    ]