from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ClientPolicy


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'account_type', 'company_name', 'email',
                    'first_name', 'last_name', 'phone', 'is_staff')
    list_filter = UserAdmin.list_filter + ('account_type',)
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('phone', 'middle_name', 'account_type', 'company_name')}),
    )


@admin.register(ClientPolicy)
class ClientPolicyAdmin(admin.ModelAdmin):
    list_display = ('user', 'policy_type', 'object_info', 'start_date', 'end_date', 'price')
    list_filter = ('policy_type',)
    search_fields = ('user__username', 'object_info')
