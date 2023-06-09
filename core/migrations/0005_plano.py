# Generated by Django 4.1.7 on 2023-04-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cliente_cancelado_cliente_data_cancelamento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do plano')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
            ],
        ),
    ]
