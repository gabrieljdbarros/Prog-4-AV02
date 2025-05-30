from .models import Servico, Agendamento
from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'criado_por')
    list_filter = ('categoria',)
    search_fields = ('nome',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ('nome',)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'servico', 'data_agendada', 'horario')
    list_filter = ('data_agendada', 'servico')
    search_fields = ('usuario__username',)
