# Generated by Django 4.0.4 on 2022-04-21 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_gatos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
