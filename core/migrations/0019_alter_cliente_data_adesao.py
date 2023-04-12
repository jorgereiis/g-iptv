# Generated by Django 4.1.7 on 2023-04-07 21:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_cliente_data_adesao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_adesao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de adesão'),
        ),
    ]
