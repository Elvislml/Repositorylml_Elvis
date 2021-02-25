# Generated by Django 3.1.4 on 2021-01-06 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0006_auto_20210105_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.CharField(choices=[('union', 'Union Libre'), ('divorciado', 'Divorciado'), ('casado', 'Casado'), ('viudo', 'Viudo'), ('separado', 'Separado'), ('soltero', 'Soltero')], default='soltero', max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], default='femenino', max_length=30),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='tipoCuenta',
            field=models.CharField(choices=[('programado', 'Programado'), ('corriente', 'Corriente'), ('ahorros', 'Ahorros')], default='ahorros', max_length=30),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(choices=[('deposito', 'Deposito'), ('retiro', 'Retiro')], default='deposito', max_length=30),
        ),
    ]
