# Generated by Django 4.1 on 2022-09-23 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contratos', '0005_alter_contratos_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratos',
            name='aprobado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contratos',
            name='disponibilidad',
            field=models.BooleanField(default=True),
        ),
    ]