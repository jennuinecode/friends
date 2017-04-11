# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-11 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='manager.User')),
            ],
        ),
    ]
