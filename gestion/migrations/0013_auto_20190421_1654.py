# Generated by Django 2.2 on 2019-04-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_auto_20190421_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dyh_project',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
