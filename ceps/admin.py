from django.contrib import admin

from .models import Estado


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ("uf", "imagem")
    search_fields = ("uf",)
    ordering = ("uf",)