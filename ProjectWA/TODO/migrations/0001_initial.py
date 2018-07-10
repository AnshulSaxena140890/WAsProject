# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-10 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskID', models.AutoField(primary_key=True, serialize=False)),
                ('taskName', models.CharField(max_length=200)),
                ('taskBrief', models.TextField()),
                ('isDone', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('doneAt', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]