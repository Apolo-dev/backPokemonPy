# Generated by Django 3.2.8 on 2021-10-27 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEquipo', '0003_equipo_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='ataques',
        ),
    ]
