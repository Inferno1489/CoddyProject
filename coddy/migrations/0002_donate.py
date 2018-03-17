# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-16 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coddy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
                ('comp', models.BooleanField()),
                ('sms', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Пожертвование',
                'verbose_name_plural': 'Пожертвования',
            },
        ),
    ]
