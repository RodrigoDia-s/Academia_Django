from django.contrib import admin

from .models import Plano


@admin.register(Plano)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "slug",
        "descricao",
        "preco",
    ]