from django.contrib import admin
from .models import ClientProduct

@admin.register(ClientProduct)
class ClientProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'price_from', 'is_active')
    list_filter = ('kind', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
