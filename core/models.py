from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Servidor(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Servidores"

    def __str__(self):
        return self.nome


class Tipos_pgto(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Tipo de pagamento"
        verbose_name_plural = "Tipos de pagamentos"

    def __str__(self):
        return self.nome


class Dispositivo(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome


class Sistema(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome


class Qtd_tela(models.Model):
    telas = models.PositiveSmallIntegerField('Quantidade de telas', unique=True)

    class Meta:
        verbose_name_plural = "Quantidade de telas"

    def __str__(self):
        return "{} tela(s)".format(self.telas)
    

class Plano(models.Model):
    MENSAL = 'Mensal'
    SEMESTRAL = 'Semestral'
    ANUAL = 'Anual'

    CHOICES = (
        (MENSAL, 'Mensal'),
        (SEMESTRAL, 'Semestral'),
        (ANUAL, 'Anual')
    )

    nome = models.CharField('Nome do plano', max_length=255, choices=CHOICES, default=MENSAL, unique=True)
    valor = models.DecimalField('Valor', max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} - {}".format(self.nome, self.valor)


class Cliente(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    indicado_por = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    data_pagamento = models.IntegerField('Data de pagamento',default=None, blank=True, null=True)
    forma_pgto = models.ForeignKey(Tipos_pgto, on_delete=models.CASCADE, verbose_name='Forma de pagamento')
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE, default=1)
    telas = models.ForeignKey(Qtd_tela, on_delete=models.CASCADE, default=1)
    data_adesao = models.DateField('Data de adesão', default=datetime.now().date())
    data_cancelamento = models.DateField('Data de cancelamento', blank=True, null=True)
    ultimo_pagamento = models.DateField('Último pagamento realizado', blank=True, null=True)
    cancelado = models.BooleanField('Cancelado', default=False)


    def save(self, *args, **kwargs):
        if self.ultimo_pagamento:
            dia_adesao = self.ultimo_pagamento.day
        else:
            dia_adesao = self.data_adesao.day

        dia_pagamento = self.definir_dia_pagamento(dia_adesao)

        self.data_pagamento = dia_pagamento

        self.definir_data_cancelamento()

        self.formatar_telefone()

        super().save(*args, **kwargs)

    def definir_dia_pagamento(self, dia_adesao):
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
        return dia_pagamento

    def definir_data_cancelamento(self):
        if self.pk:
            old_value = Cliente.objects.get(pk=self.pk).cancelado
            if old_value == False and self.cancelado == True:
                self.data_cancelamento = datetime.now().date()
            elif old_value == True and self.cancelado == False:
                self.data_cancelamento = None

    def formatar_telefone(self):
        if not self.telefone.startswith("55"):
            self.telefone = "55" + self.telefone

    def __str__(self):
        return self.nome


class Mensalidade(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    valor = models.DecimalField('Valor', max_digits=5, decimal_places=2, default=None)
    dt_vencimento = models.DateField('Data de vencimento', default=datetime.now().date()+ timezone.timedelta(days=30))
    dt_pagamento = models.DateField('Data de pagamento', default=None, null=True, blank=True)
    pgto = models.BooleanField('Pago',default=False)
    cancelado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Atualiza a data de pagamento se a mensalidade for paga
        if self.pk:
            old_value = Mensalidade.objects.get(pk=self.pk).pgto
            if old_value == False and self.pgto == True:
                self.dt_pagamento = datetime.now().date()
                
            elif old_value == True and self.pgto == False:
                self.dt_pagamento = None

        super().save(*args, **kwargs)
        
        # Cria uma nova mensalidade se dt_pagamento e pgto forem verdadeiros
        if self.dt_pagamento and self.pgto:
            Mensalidade.objects.create(
                cliente=self.cliente,
                valor=self.cliente.plano.valor,
                dt_vencimento=self.dt_pagamento + timezone.timedelta(days=30)
            )

    def __str__(self):
        return str('[{}] {} - {}'.format(self.dt_vencimento.strftime('%d/%m/%Y'), self.valor, self.cliente))

# Atualiza o último pagamento do cliente quando uma mensalidade é salva
@receiver(post_save, sender=Mensalidade)
def atualiza_ultimo_pagamento(sender, instance, **kwargs):
    cliente = instance.cliente
    if instance.dt_pagamento and instance.pgto:
        if not cliente.ultimo_pagamento or instance.dt_pagamento > cliente.ultimo_pagamento:
            cliente.ultimo_pagamento = instance.dt_pagamento
            cliente.save()

# Cria uma nova mensalidade quando um novo cliente for criado
@receiver(post_save, sender=Cliente)
def criar_mensalidade(sender, instance, created, **kwargs):
    if created:
        Mensalidade.objects.create(cliente=instance, valor=instance.plano.valor)