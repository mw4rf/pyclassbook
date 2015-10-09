# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20151009_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='has_marks',
        ),
    ]
