# Generated by Django 2.0.7 on 2018-08-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_auto_20180727_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentes',
            name='cartao_id',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='componentes',
            name='estatos',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
