python --version

python -m venv venv

venv/Scripts/activate

Se der erro ( vai dar erro ) -> Set-ExecutionPolicy Unrestrict

pip install django

django-admin --version

instalar a extensão SQLite Viwer

django-admin startproject aula .

python manage.py runserver

python manage.py migrate

python manage.py createsuperuser

python manage.py startapp produtos

Adicionar script abaixo no caminho -> produtos -> models.py
```
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField(null=False)****
    valor = models.FloatField(null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
return self.nome
```

Adicionar script abaixo no caminho -> produtos -> admin.py

```
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
```

python manage.py makemigrations