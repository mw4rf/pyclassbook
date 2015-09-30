# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20150928_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mark',
            options={'verbose_name': 'Note'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Étudiant'},
        ),
        migrations.AddField(
            model_name='student',
            name='comments',
            field=models.TextField(blank=True, default='', verbose_name='Commentaires'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Commentaires'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='mark',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(to='students.Student', verbose_name='Étudiant'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(to='exams.Subject', verbose_name='Sujet'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth',
            field=models.DateField(verbose_name='Date de naissance', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course', verbose_name='Cours'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email_alt',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-Mail alternatif'),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=100, verbose_name='Nom de famille'),
        ),
        migrations.AlterField(
            model_name='student',
            name='native_lang',
            field=models.BooleanField(default=True, verbose_name='Français langue maternelle ?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='third_time',
            field=models.BooleanField(default=False, verbose_name='Tiers temps ?'),
        ),
    ]
