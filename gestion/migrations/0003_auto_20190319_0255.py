# Generated by Django 2.1.7 on 2019-03-19 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20190319_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cronograma',
            name='numero',
        ),
        migrations.AddField(
            model_name='cronograma',
            name='tipo',
            field=models.CharField(choices=[('mantenimiento', 'mantenimiento'), ('calibracion', 'calibracion')], default='mantenimiento', max_length=100),
        ),
    ]
