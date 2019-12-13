from django.db import models

# Create your models here.

import django_tables2 as tables


class UpdateInfo(models.Model):
    NAME = models.CharField(primary_key=True, max_length=120, null=False, verbose_name="Package Name")
    VERSION = models.CharField(max_length=120, null=False, verbose_name="Version")
    ARCH = models.CharField(max_length=120, null=False, verbose_name="Arch")
    REPO = models.CharField(max_length=120, null=False, verbose_name="Repo")
    DETAIL = models.BooleanField(null=True, default=True, verbose_name="Detail")

    # 指定database table name
    class Meta:
        db_table = "update_info"


class UpdateDetail(models.Model):
    NAME = models.CharField(primary_key=True, max_length=120, null=False, verbose_name="Package Name")
    VERSION = models.CharField(max_length=120, null=False, verbose_name="Version")
    ARCH = models.CharField(max_length=120, null=False, verbose_name="Arch")
    REPO = models.CharField(max_length=120, null=False, verbose_name="Repo")
