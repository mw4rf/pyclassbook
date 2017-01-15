# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 10:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_mark_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mark',
            options={'verbose_name': 'Mark'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student'},
        ),
        migrations.AlterField(
            model_name='mark',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='mark',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='Mark'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Subject', verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='Birth date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='comments',
            field=models.TextField(blank=True, default='', verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course', verbose_name='Courses'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email_alt',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Alternative e-mail'),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='firstname'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=100, verbose_name='lastname'),
        ),
        migrations.AlterField(
            model_name='student',
            name='native_lang',
            field=models.BooleanField(default=True, verbose_name='Native language ?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='third_time',
            field=models.BooleanField(default=False, verbose_name='Has a third time ?'),
        ),
    ]
