# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filearr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=512, unique=True)),
                ('mirrors', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'filearr',
            },
        ),
        migrations.CreateModel(
            name='Hexhash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=512, unique=True)),
                ('bithex', models.CharField(max_length=512)),
            ],
            options={
                'managed': False,
                'db_table': 'hexhash',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=64, unique=True)),
                ('baseurl', models.CharField(max_length=128)),
                ('baseurl_ftp', models.CharField(max_length=128)),
                ('baseurl_rsync', models.CharField(max_length=128)),
                ('enabled', models.BooleanField()),
                ('status_baseurl', models.BooleanField()),
                ('region', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=2)),
                ('asn', models.IntegerField()),
                ('prefix', models.CharField(max_length=18)),
                ('score', models.SmallIntegerField()),
                ('scan_fpm', models.IntegerField()),
                ('last_scan', models.DateTimeField(blank=True, null=True)),
                ('comment', models.TextField()),
                ('operator_name', models.CharField(max_length=128)),
                ('operator_url', models.CharField(max_length=128)),
                ('public_notes', models.CharField(max_length=512)),
                ('admin', models.CharField(max_length=128)),
                ('admin_email', models.CharField(max_length=128)),
                ('lat', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('country_only', models.BooleanField()),
                ('region_only', models.BooleanField()),
                ('as_only', models.BooleanField()),
                ('prefix_only', models.BooleanField()),
                ('other_countries', models.CharField(max_length=512)),
                ('file_maxsize', models.IntegerField()),
                ('ipv6_only', models.BooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'server',
            },
        ),
        migrations.CreateModel(
            name='Hash',
            fields=[
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.Filearr')),
                ('mtime', models.IntegerField()),
                ('size', models.BigIntegerField()),
                ('md5', models.BinaryField()),
                ('sha1', models.BinaryField()),
                ('sha256', models.BinaryField()),
                ('sha1piecesize', models.IntegerField()),
                ('sha1pieces', models.BinaryField()),
                ('btih', models.BinaryField()),
                ('pgp', models.TextField()),
                ('zblocksize', models.SmallIntegerField()),
                ('zhashlens', models.CharField(blank=True, max_length=8, null=True)),
                ('zsums', models.BinaryField()),
            ],
            options={
                'managed': False,
                'db_table': 'hash',
            },
        ),
    ]