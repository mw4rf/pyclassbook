# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='comments',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='place',
            field=models.CharField(max_length=254, default=''),
        ),
        migrations.AddField(
            model_name='exam',
            name='time_allowed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='kind',
            field=models.CharField(max_length=254, default=''),
        ),
        migrations.AddField(
            model_name='subject',
            name='title',
            field=models.TextField(default='', blank=True),
        ),
    ]
