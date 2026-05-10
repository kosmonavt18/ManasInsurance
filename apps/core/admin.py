from django.contrib import admin
from .models import SiteSettings, InsuranceCase, Branch


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'email')


@admin.register(InsuranceCase)
class InsuranceCaseAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'phone')
