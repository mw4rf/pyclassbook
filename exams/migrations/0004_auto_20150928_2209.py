# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_exam_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 20, 8, 52, 763574, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 20, 9, 1, 779885, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 20, 9, 7, 596043, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 20, 9, 13, 292142, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exam',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True, editable=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True, editable=False),
        ),
    ]
