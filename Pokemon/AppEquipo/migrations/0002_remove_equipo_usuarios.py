# Generated by Django 3.2.8 on 2021-10-25 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEquipo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='usuarios',
        ),
    ]
