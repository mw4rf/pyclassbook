# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20150928_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True, editable=False),
        ),
    ]
