# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150928_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Cours'},
        ),
        migrations.AlterField(
            model_name='course',
            name='comments',
            field=models.TextField(blank=True, verbose_name='Commentaires'),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(blank=True, verbose_name='Date de fin'),
        ),
        migrations.AlterField(
            model_name='course',
            name='kind',
            field=models.CharField(max_length=254, blank=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(max_length=10, blank=True, verbose_name='Niveau'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=254, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='course',
            name='place',
            field=models.CharField(max_length=254, blank=True, verbose_name='Lieu'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, verbose_name='Date de début'),
        ),
    ]
