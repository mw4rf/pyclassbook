# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20150808_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
