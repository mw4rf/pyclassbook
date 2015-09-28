# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email_alt',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='native_lang',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='third_time',
            field=models.BooleanField(default=False),
        ),
    ]
