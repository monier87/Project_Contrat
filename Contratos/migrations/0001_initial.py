# Generated by Django 4.1 on 2022-08-25 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=50)),
                ('Obsevaciones', models.CharField(max_length=255)),
                ('Objeto', models.CharField(max_length=255)),
                ('CodigoContrato', models.CharField(max_length=10)),
                ('CUP', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('Creado', models.DateTimeField(auto_now_add=True)),
                ('Modificado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'contrato',
                'verbose_name_plural': 'contratos',
            },
        ),
    ]
