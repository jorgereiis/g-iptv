# Generated by Django 4.1.7 on 2023-04-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_cliente_telas'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='data_pagamento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
