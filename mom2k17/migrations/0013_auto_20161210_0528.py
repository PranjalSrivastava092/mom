# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom2k17', '0012_auto_20161210_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='message',
            field=models.TextField(default='', max_length=2000),
        ),
    ]