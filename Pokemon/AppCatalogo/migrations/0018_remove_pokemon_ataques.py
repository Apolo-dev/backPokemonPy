# Generated by Django 3.2.5 on 2021-10-03 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCatalogo', '0017_auto_20211002_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='ataques',
        ),
    ]
