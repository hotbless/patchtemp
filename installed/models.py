from django.db import models

# Create your models here.


# SELECT * FROM "INSTALLED_INFO"

import django_tables2 as tables

from django.db import connection


def installed_info_sql():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "INSTALLED_INFO"')
        row = cursor.fetchall()

    return row
