# Generated by Django 4.1.7 on 2023-03-26 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_qtd_telas_qtd_tela_rename_servidores_servidor'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='data_adesao',
            field=models.DateField(default=datetime.date(2023, 3, 26), verbose_name='Data de adesão'),
        ),
    ]