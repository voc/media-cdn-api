# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'managed': False,
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtree_name', models.CharField(max_length=128)),
                ('markers', models.CharField(max_length=512)),
            ],
            options={
                'managed': False,
                'db_table': 'marker',
            },
        ),
        migrations.CreateModel(
            name='Pfx2Asn',
            fields=[
                ('pfx', models.TextField(primary_key=True, serialize=False)),
                ('asn', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'pfx2asn',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'managed': False,
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.TextField()),
                ('major', models.IntegerField()),
                ('minor', models.IntegerField()),
                ('patchlevel', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'version',
            },
        ),
    ]