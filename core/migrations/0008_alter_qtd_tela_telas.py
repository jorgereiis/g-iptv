# Generated by Django 4.1.7 on 2023-04-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_nome_qtd_tela_telas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qtd_tela',
            name='telas',
            field=models.PositiveSmallIntegerField(verbose_name='Quantidade de telas'),
        ),
    ]
