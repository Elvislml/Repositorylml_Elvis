# Generated by Django 3.1.4 on 2021-01-06 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0004_auto_20210105_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.CharField(choices=[('separado', 'Separado'), ('casado', 'Casado'), ('union', 'Union Libre'), ('viudo', 'Viudo'), ('divorciado', 'Divorciado'), ('soltero', 'Soltero')], default='soltero', max_length=30),
        ),
    ]
