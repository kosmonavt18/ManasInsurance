from django.contrib import admin
from .models import AutoProduct, TariffRow


class TariffInline(admin.TabularInline):
    model = TariffRow
    extra = 1


@admin.register(AutoProduct)
class AutoProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'price_from', 'has_calculator', 'is_active')
    list_filter = ('kind', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TariffInline]
