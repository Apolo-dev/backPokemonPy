# Generated by Django 3.2.5 on 2021-10-02 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCatalogo', '0003_auto_20211002_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={'ordering': ['-created']},
        ),
    ]
