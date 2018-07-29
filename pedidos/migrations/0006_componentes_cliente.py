# Generated by Django 2.0.7 on 2018-07-27 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('pedidos', '0005_componentes'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentes',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]
