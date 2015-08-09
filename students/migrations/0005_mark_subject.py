# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20150809_1147'),
        ('students', '0004_mark_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(default=1, to='exams.Subject'),
            preserve_default=False,
        ),
    ]
