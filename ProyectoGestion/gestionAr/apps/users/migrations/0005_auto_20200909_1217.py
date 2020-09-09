# Generated by Django 3.0 on 2020-09-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200908_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='medico',
            name='nombres',
        ),
        migrations.AddField(
            model_name='medico',
            name='nombres_y_apellido',
            field=models.CharField(default='MARIA GOMEZ', max_length=30),
        ),
        migrations.AddField(
            model_name='paciente',
            name='medico',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
