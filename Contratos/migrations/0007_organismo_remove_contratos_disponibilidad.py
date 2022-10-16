# Generated by Django 4.1 on 2022-09-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contratos', '0006_contratos_aprobado_contratos_disponibilidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('codigoRUP', models.CharField(max_length=50)),
                ('banco', models.CharField(max_length=50)),
                ('cuentaMN', models.CharField(max_length=50)),
                ('cuentaMLC', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Organismo',
                'verbose_name_plural': 'Organismos',
            },
        ),
        migrations.RemoveField(
            model_name='contratos',
            name='disponibilidad',
        ),
    ]
