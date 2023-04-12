# Generated by Django 4.1.7 on 2023-04-09 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_cliente_nome_alter_cliente_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_adesao',
            field=models.DateField(auto_now_add=True, verbose_name='Data de adesão'),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mensalidades', to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True, verbose_name='Valor'),
        ),
    ]
