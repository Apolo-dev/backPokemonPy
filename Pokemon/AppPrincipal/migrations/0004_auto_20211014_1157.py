# Generated by Django 3.2.5 on 2021-10-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrincipal', '0003_alter_pokemon_ataques'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='tipe_pokemon',
            new_name='type_pokemon',
        ),
        migrations.AddField(
            model_name='ataque',
            name='type_attack',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
