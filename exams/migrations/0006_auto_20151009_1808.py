# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20150930_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='coeff',
            field=models.IntegerField(default=1, verbose_name='Coefficient'),
        ),
        migrations.AddField(
            model_name='subject',
            name='has_marks',
            field=models.BooleanField(default=True, verbose_name='Has Marks ?'),
        ),
    ]
