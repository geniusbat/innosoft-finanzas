# Generated by Django 3.2.8 on 2021-12-28 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('necesidades', '0002_auto_20211225_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comite', models.CharField(max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Necesidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('cantidadNecesitada', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('comite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='necesidades.comite')),
            ],
        ),
    ]
