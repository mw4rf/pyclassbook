# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20151008_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth',
            field=models.DateField(null=True, blank=True, verbose_name='Date de naissance'),
        ),
    ]
