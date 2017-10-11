# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('branch', models.CharField(max_length=128)),
                ('semester', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=128)),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Student')),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Subject'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Lecture'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Subject'),
        ),
    ]
