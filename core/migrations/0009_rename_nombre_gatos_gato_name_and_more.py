# Generated by Django 4.0.4 on 2022-04-26 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_gatos_postulacion_gato_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gatos',
            old_name='nombre',
            new_name='gato_name',
        ),
        migrations.RenameField(
            model_name='postulacion',
            old_name='gato_name',
            new_name='gato',
        ),
    ]
