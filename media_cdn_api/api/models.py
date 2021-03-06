# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Server(models.Model):
    identifier = models.CharField(unique=True, max_length=64)
    baseurl = models.CharField(max_length=128)
    baseurl_ftp = models.CharField(max_length=128)
    baseurl_rsync = models.CharField(max_length=128)
    enabled = models.BooleanField()
    status_baseurl = models.BooleanField()
    region = models.CharField(max_length=2)
    country = models.CharField(max_length=2)
    asn = models.IntegerField()
    prefix = models.CharField(max_length=18)
    score = models.SmallIntegerField()
    scan_fpm = models.IntegerField()
    last_scan = models.DateTimeField(blank=True, null=True)
    comment = models.TextField()
    operator_name = models.CharField(max_length=128)
    operator_url = models.CharField(max_length=128)
    public_notes = models.CharField(max_length=512)
    admin = models.CharField(max_length=128)
    admin_email = models.CharField(max_length=128)
    lat = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    lng = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    country_only = models.BooleanField()
    region_only = models.BooleanField()
    as_only = models.BooleanField()
    prefix_only = models.BooleanField()
    other_countries = models.CharField(max_length=512)
    file_maxsize = models.IntegerField()
    ipv6_only = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'server'
