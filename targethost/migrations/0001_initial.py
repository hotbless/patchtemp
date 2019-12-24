# Generated by Django 3.0 on 2019-12-24 11:47

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
                ('TIME', models.DateTimeField(max_length=120, verbose_name='Scan Time')),
                ('IP', models.GenericIPAddressField(verbose_name='IP')),
            ],
            options={
                'db_table': 'installed_info',
            },
        ),
        migrations.CreateModel(
            name='UpdateInfoDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=120, verbose_name='Package Name')),
                ('VERSION', models.CharField(max_length=120, verbose_name='Version')),
                ('ARCH', models.CharField(max_length=120, verbose_name='Arch')),
                ('REPO', models.CharField(max_length=120, verbose_name='Repo')),
                ('TIME', models.DateTimeField(max_length=120, verbose_name='Scan Time')),
                ('IP', models.GenericIPAddressField(verbose_name='IP')),
            ],
            options={
                'db_table': 'update_info_details',
                'unique_together': {('NAME', 'VERSION', 'ARCH', 'REPO', 'IP')},
            },
        ),
        migrations.CreateModel(
            name='UpdateInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=120, verbose_name='Package Name')),
                ('VERSION', models.CharField(max_length=120, verbose_name='Version')),
                ('ARCH', models.CharField(max_length=120, verbose_name='Arch')),
                ('REPO', models.CharField(max_length=120, verbose_name='Repo')),
                ('TIME', models.DateTimeField(max_length=120, verbose_name='Scan Time')),
                ('IP', models.GenericIPAddressField(verbose_name='IP')),
            ],
            options={
                'db_table': 'update_info',
                'unique_together': {('NAME', 'VERSION', 'ARCH', 'REPO', 'IP')},
            },
        ),
    ]
