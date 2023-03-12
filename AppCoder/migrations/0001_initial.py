# Generated by Django 4.1.7 on 2023-03-12 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automotor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=16)),
                ('nchasis', models.CharField(max_length=10)),
                ('nmotor', models.CharField(max_length=10)),
                ('npatente', models.CharField(max_length=7)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=16)),
                ('veiculos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
                ('user', models.CharField(max_length=16)),
            ],
        ),
    ]