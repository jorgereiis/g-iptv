from django.contrib import admin
from .models import Servidor, Tipos_pgto, Dispositivo, Sistema, Qtd_tela, Cliente, Plano, Mensalidade

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nome',
                    'telefone',
                    'servidor',
                    'dispositivo',
                    'sistema',
                    'data_pagamento',
                    'forma_pgto',
                    'plano',
                    'telas',
                    'data_adesao',
                    'data_cancelamento',
                    'ultimo_pagamento',
                    'cancelado')

class MensalidadeAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'cliente',
                    'dt_vencimento',
                    'dt_pagamento',
                    'valor',
                    'pgto',
                    'cancelado')
    
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor')

admin.site.register(Mensalidade, MensalidadeAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Plano, PlanoAdmin)
admin.site.register(Dispositivo)
admin.site.register(Tipos_pgto)
admin.site.register(Qtd_tela)
admin.site.register(Servidor)
admin.site.register(Sistema)