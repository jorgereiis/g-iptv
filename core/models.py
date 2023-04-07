from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Servidor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Tipos_pgto(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Dispositivo(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Sistema(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Qtd_tela(models.Model):
    telas = models.PositiveSmallIntegerField('Quantidade de telas')

    def __str__(self):
        return "{} tela(s)".format(self.telas)
    

class Plano(models.Model):
    nome = models.CharField('Nome do plano', max_length=255)
    valor = models.DecimalField('Valor', max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} - {}".format(self.nome, self.valor)


class Cliente(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    data_pagamento = models.IntegerField(default=None, blank=True, null=True)
    forma_pgto = models.ForeignKey(Tipos_pgto, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE, default=None)
    telas = models.ForeignKey(Qtd_tela, on_delete=models.CASCADE, default=None)
    data_adesao = models.DateField('Data de adesão', default=timezone.now().date())
    data_cancelamento = models.DateField('Data de cancelamento', blank=True, null=True)
    ultimo_pagamento = models.DateField('Último pagamento realizado', blank=True, null=True)
    cancelado = models.BooleanField('Cancelado', default=False)


    def save(self, *args, **kwargs):
        if self.ultimo_pagamento:
            dia_adesao = self.ultimo_pagamento.day
        else:
            dia_adesao = self.data_adesao.day

        # Define data de pagamento com base na data do último pagamento realizado
        if dia_adesao in range(3, 8):
            dia_pagamento = 5
        elif dia_adesao in range(8, 13):
            dia_pagamento = 10
        elif dia_adesao in range(13, 18):
            dia_pagamento = 15
        elif dia_adesao in range(18, 23):
            dia_pagamento = 20
        elif dia_adesao in range(23, 28):
            dia_pagamento = 25
        else:
            dia_pagamento = 30

        # Define o valor do atributo 'data_pagamento'
        self.data_pagamento = dia_pagamento

        if self.pk: # condicional para definição do atributo 'data_cancelamento'
            
            old_value = Cliente.objects.get(pk=self.pk).cancelado # obtém o valor do campo 'cancelado'
            if old_value == False and self.cancelado == True: # verifica se o valor foi alterado de False para True
                self.data_cancelamento = timezone.now().date() # Define a data atual para o campo 'data_cancelamento'
            
            elif old_value == True and self.cancelado == False: # verifica se o valor foi alterado de True para False
                self.data_cancelamento = None # define como 'None' o valor do campo 'data_cancelamento', deixando limpo novamente

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

