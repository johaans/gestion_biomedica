# Generated by Django 2.2 on 2019-05-05 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0017_auto_20190421_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='marca',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='MARCA'),
        ),
    ]