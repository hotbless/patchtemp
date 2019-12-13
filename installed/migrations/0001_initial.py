# Generated by Django 3.0 on 2019-12-13 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstalledInfo',
            fields=[
                ('NAME', models.CharField(max_length=120, primary_key=True, serialize=False, verbose_name='Package Name')),
                ('VERSION', models.CharField(max_length=120, verbose_name='Version')),
                ('ARCH', models.CharField(max_length=120, verbose_name='Arch')),
            ],
            options={
                'db_table': 'installed_info',
            },
        ),
    ]
