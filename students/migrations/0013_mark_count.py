# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20151008_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='count',
            field=models.BooleanField(verbose_name='Count this in the average ?', default=True),
        ),
    ]
