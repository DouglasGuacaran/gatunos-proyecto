# Generated by Django 4.0.4 on 2022-04-27 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_nombre_gatos_gato_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulacion',
            name='direccion',
            field=models.CharField(default='SOME STRING', max_length=250),
        ),
    ]
