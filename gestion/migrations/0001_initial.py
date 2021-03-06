# Generated by Django 2.1.7 on 2019-03-19 07:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cronograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField(verbose_name='fecha')),
            ],
        ),
        migrations.CreateModel(
            name='equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, verbose_name='Names')),
                ('modelo', models.CharField(max_length=25, verbose_name='Lastname')),
                ('activo', models.CharField(blank=True, max_length=25, null=True, verbose_name='Surname')),
                ('ubicacion', models.CharField(blank=True, max_length=25, null=True, verbose_name='Surname')),
                ('serie', models.CharField(max_length=15, unique=True, verbose_name='Document')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cronograma',
            name='rel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.equipo'),
        ),
    ]
