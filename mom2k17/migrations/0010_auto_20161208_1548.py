# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom2k17', '0009_auto_20161208_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='momid',
            field=models.CharField(max_length=15),
        ),
    ]