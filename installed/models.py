from django.db import models

# Create your models here.


# SELECT * FROM "INSTALLED_INFO"

import django_tables2 as tables


class InstalledInfo(models.Model):
    NAME = models.CharField(primary_key=True, max_length=120, null=False, verbose_name="Package Name")
    VERSION = models.CharField(max_length=120, null=False, verbose_name="Version")
    ARCH = models.CharField(max_length=120, null=False, verbose_name="Arch")

    class Meta:
        db_table = "installed_info"



# unique = True

# def installed_info_sql():
#     with connection.cursor() as cursor:
#         cursor.execute('SELECT * FROM "INSTALLED_INFO"')
#         row = cursor.fetchall()
#
#     return row
