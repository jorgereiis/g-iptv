from django.contrib import admin
from .models import Servidor, Tipos_pgto, Dispositivo, Sistema, Qtd_tela, Cliente, Plano

# Register your models here.

admin.site.register(Servidor)
admin.site.register(Tipos_pgto)
admin.site.register(Dispositivo)
admin.site.register(Sistema)
admin.site.register(Qtd_tela)
admin.site.register(Cliente)
admin.site.register(Plano)