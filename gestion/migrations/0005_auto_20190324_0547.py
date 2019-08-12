# Generated by Django 2.1.7 on 2019-03-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_auto_20190319_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='calibracion',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='N/A', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='cronograma_calibracion',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='equipo',
            name='cronograma_mantenimiento',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='equipo',
            name='factura',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='no', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='factura_file',
            field=models.FileField(blank=True, null=True, upload_to='facturas'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='guia_rapida',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='N/A', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='importacion',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='no', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='importacion_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='equipo',
            name='importador',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='equipo',
            name='invima',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='N/A', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='invima_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='equipo',
            name='mantenimiento',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='N/A', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='manual_funcionamiento',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='N/A', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='manual_instalacion',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='N/A', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='manual_mantenimiento',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='N/A', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='manual_usuario',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no'), ('N/A', 'N/A')], default='N/A', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='pais',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='equipo',
            name='riesgo',
            field=models.CharField(choices=[('1', 'I'), ('2A', 'IIA'), ('2B', 'IIB'), ('3', 'III'), ('N/A', 'N/A')], default='N/A', max_length=3),
        ),
        migrations.AddField(
            model_name='equipo',
            name='ubicacion_manuales',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='equipo',
            name='uso',
            field=models.CharField(choices=[('estetica', 'estetica'), ('diagnostico', 'diagnostico'), ('laboratorio', 'laboratorio'), ('prevencion', 'prevencion'), ('rehabilitacion', 'rehabilitacion'), ('soporte vital', 'soporte vital'), ('tratamiento', 'tratamiento'), ('N/A', 'N/A')], default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ubicacion',
            field=models.CharField(choices=[('quirofano 1', 'quirofano 1'), ('quirofano 2', 'quirofano 2'), ('quirofano 3', 'quirofano 3'), ('quirofano 4', 'quirofano 4'), ('central de esterilizacion', 'central de esterilizacion'), ('recuperacion', 'recuperacion'), ('preparacion', 'preparacion'), ('procedimientos menores', 'procedimientos menores'), ('consultorio anestesia', 'consultorio anestesia'), ('consultorio 2', 'consultorio 2'), ('otro', 'otro')], default='otro', max_length=100, verbose_name='UBICACION'),
        ),
    ]
