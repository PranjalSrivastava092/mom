# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom2k17', '0008_auto_20161208_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='message',
            field=models.TextField(max_length=2000),
        ),
    ]