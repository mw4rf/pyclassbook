# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_remove_subject_has_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='coeff',
        ),
        migrations.AddField(
            model_name='exam',
            name='coeff',
            field=models.IntegerField(default=1, verbose_name='Coefficient'),
        ),
    ]
