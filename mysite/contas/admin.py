from django.contrib import admin

# Register your models here.
from .models import Conta

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'pago')
    list_filter = ('pago',)
    search_fields = ('descricao',)