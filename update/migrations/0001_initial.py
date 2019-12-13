# Generated by Django 3.0 on 2019-12-13 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateDetail',
            fields=[
                ('NAME', models.CharField(max_length=120, primary_key=True, serialize=False, verbose_name='Package Name')),
                ('VERSION', models.CharField(max_length=120, verbose_name='Version')),
                ('ARCH', models.CharField(max_length=120, verbose_name='Arch')),
                ('REPO', models.CharField(max_length=120, verbose_name='Repo')),
            ],
        ),
        migrations.CreateModel(
            name='UpdateInfo',
            fields=[
                ('NAME', models.CharField(max_length=120, primary_key=True, serialize=False, verbose_name='Package Name')),
                ('VERSION', models.CharField(max_length=120, verbose_name='Version')),
                ('ARCH', models.CharField(max_length=120, verbose_name='Arch')),
                ('REPO', models.CharField(max_length=120, verbose_name='Repo')),
                ('DETAIL', models.BooleanField(default=False, verbose_name='Detail')),
            ],
            options={
                'db_table': 'update_info',
            },
        ),
    ]
