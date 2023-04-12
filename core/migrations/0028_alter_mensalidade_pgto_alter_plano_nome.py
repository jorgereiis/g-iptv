# Generated by Django 4.1.7 on 2023-04-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_cliente_data_adesao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalidade',
            name='pgto',
            field=models.BooleanField(default=False, verbose_name='Pago'),
        ),
        migrations.AlterField(
            model_name='plano',
            name='nome',
            field=models.CharField(choices=[('Mensal', 'Mensal'), ('Semestral', 'Semestral'), ('Anual', 'Anual')], max_length=255, unique=True, verbose_name='Nome do plano'),
        ),
    ]