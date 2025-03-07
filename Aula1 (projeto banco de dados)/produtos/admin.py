from django.contrib import admin
from .models import Produto  # Importa o modelo Produto

@admin.register(Produto)  # Registra o modelo no Django Admin
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'data_criacao', 'data_modificacao')  # Colunas visíveis na listagem
    search_fields = ('nome', 'descricao')  # Adiciona barra de pesquisa
    list_filter = ('data_criacao', 'data_modificacao')  # Adiciona filtros laterais
    ordering = ('-data_criacao',)
    fieldsets = (
        ("Informações Gerais", {"fields": ("nome", "descricao", "valor")}),
        ("Datas", {"fields": ("data_criacao", "data_modificacao")}),
    ) 
    readonly_fields = ('data_criacao', 'data_modificacao')