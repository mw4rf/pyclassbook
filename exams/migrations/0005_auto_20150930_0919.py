# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20150928_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'Examen'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Sujet'},
        ),
        migrations.AlterField(
            model_name='exam',
            name='comments',
            field=models.TextField(default='', blank=True, verbose_name='Commentaires'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(to='courses.Course', verbose_name='Cours'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='name',
            field=models.CharField(default='', max_length=254, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='place',
            field=models.CharField(default='', max_length=254, verbose_name='Lieu'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='time_allowed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps alloué'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='exam',
            field=models.ForeignKey(to='exams.Exam', verbose_name='Examen'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='kind',
            field=models.CharField(default='', max_length=254, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.TextField(default='', blank=True, verbose_name='Titre'),
        ),
    ]
