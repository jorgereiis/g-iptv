# Generated by Django 4.1.7 on 2023-04-07 21:39

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_cliente_indicado_por_alter_cliente_data_adesao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_pagamento',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Data de pagamento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='forma_pgto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipos_pgto', verbose_name='Forma de pagamento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Número de telefone (xx) xxxx-xxxx', max_length=128, null=True, region=None),
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cliente')),
            ],
        ),
    ]