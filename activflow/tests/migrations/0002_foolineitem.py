# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 22:34
from __future__ import unicode_literals

import activflow.tests.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plugh', models.CharField(max_length=200, validators=[activflow.tests.validators.validate_initial_cap], verbose_name='Plugh')),
                ('thud', models.CharField(choices=[('GR', 'Grault'), ('GA', 'Garply')], max_length=30, verbose_name='Thud')),
                ('foo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Foo')),
            ],
        ),
    ]
