# Generated by Django 4.0.4 on 2022-04-26 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_ciudad_postulacion_comunas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postulacion',
            old_name='gatos',
            new_name='gato_name',
        ),
    ]