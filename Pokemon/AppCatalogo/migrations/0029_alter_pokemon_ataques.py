# Generated by Django 3.2.5 on 2021-10-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCatalogo', '0028_alter_ataque_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='ataques',
            field=models.ManyToManyField(to='AppCatalogo.Ataque', verbose_name='ataques'),
        ),
    ]
