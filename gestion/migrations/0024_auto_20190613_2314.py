# Generated by Django 2.2 on 2019-06-14 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0023_auto_20190505_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='activo',
            field=models.CharField(blank=True, help_text=' <strong>Para Equipos Alquilados Ingrese El Rango <em>De 200 En Adelante</em>.</strong>', max_length=25, null=True, unique=True, verbose_name='ACTIVO'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='manual_funcionamiento',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='no', max_length=3),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='manual_instalacion',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='no', max_length=3),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='manual_mantenimiento',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='no', max_length=3),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='manual_usuario',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='no', max_length=3),
        ),
    ]
