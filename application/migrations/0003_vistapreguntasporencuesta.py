# Generated by Django 4.2.7 on 2023-11-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_remove_perfil_id_permiso_permisos_id_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='VistaPreguntasPorEncuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pregunta', models.IntegerField()),
                ('pregunta', models.CharField(max_length=300)),
                ('tema', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'vista_preguntas_por_encuesta',
                'managed': False,
            },
        ),
    ]