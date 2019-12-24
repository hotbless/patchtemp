from django.db import models

# Create your models here.


# SELECT * FROM "INSTALLED_INFO"

import django_tables2 as tables


class InstalledInfo(models.Model):
    NAME = models.CharField(primary_key=True, max_length=120, null=False, verbose_name="Package Name")
    VERSION = models.CharField(max_length=120, null=False, verbose_name="Version")
    ARCH = models.CharField(max_length=120, null=False, verbose_name="Arch")
    TIME = models.DateTimeField(max_length=120, null=False, verbose_name="Scan Time")
    IP = models.GenericIPAddressField(max_length=120, null=False, verbose_name="IP")

    class Meta:
        db_table = "installed_info"


class UpdateInfo(models.Model):
    # NAME = models.CharField(primary_key=True, max_length=120, null=False, verbose_name="Package Name")
    NAME = models.CharField(max_length=120, null=False, verbose_name="Package Name")
    VERSION = models.CharField(max_length=120, null=False, verbose_name="Version")
    ARCH = models.CharField(max_length=120, null=False, verbose_name="Arch")
    REPO = models.CharField(max_length=120, null=False, verbose_name="Repo")
    TIME = models.DateTimeField(max_length=120, null=False, verbose_name="Scan Time")
    # TIME = models.CharField(max_length=120, null=False, verbose_name="Scan Time")
    IP = models.GenericIPAddressField(max_length=120, null=False, verbose_name="IP")
    # DETAIL = models.CharField(max_length=120, null=False, default='base', verbose_name="Detail")

    # 指定database table name
    class Meta:
        unique_together = ('NAME', 'VERSION', 'ARCH', 'REPO', 'IP')
        db_table = "update_info"


class UpdateInfoDetails(models.Model):
    NAME = models.CharField(max_length=120, null=False, verbose_name="Package Name")
    VERSION = models.CharField(max_length=120, null=False, verbose_name="Version")
    ARCH = models.CharField(max_length=120, null=False, verbose_name="Arch")
    REPO = models.CharField(max_length=120, null=False, verbose_name="Repo")
    TIME = models.DateTimeField(max_length=120, null=False, verbose_name="Scan Time")
    IP = models.GenericIPAddressField(max_length=120, null=False, verbose_name="IP")

    class Meta:
        unique_together = ('NAME', 'VERSION', 'ARCH', 'REPO', 'IP')
        db_table = "update_info_details"



# unique = True

# def installed_info_sql():
#     with connection.cursor() as cursor:
#         cursor.execute('SELECT * FROM "INSTALLED_INFO"')
#         row = cursor.fetchall()
#
#     return row