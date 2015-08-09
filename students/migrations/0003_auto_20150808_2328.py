# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20150808_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 8, 8, 21, 28, 28, 373743, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 8, 8, 21, 28, 38, 270233, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mark',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
