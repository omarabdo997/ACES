# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-08-15 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=400)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
