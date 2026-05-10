from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import Application


class CategoryFilter(admin.SimpleListFilter):
    """
    Фильтр по укрупнённым категориям заявок.
    Категории: все, авто, имущество, путешествия, жизнь, корпоративные, частные.
    """
    title = _('Категория')
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return (
            ('all', _('Все')),
            ('auto', _('Авто (ОСАГО / КАСКО / ДСАГО)')),
            ('property', _('Имущество')),
            ('travel', _('Путешествия')),
            ('life', _('Жизнь')),
            ('corporate', _('Корпоративные')),
            ('individual', _('Частные')),
        )

    def queryset(self, request, queryset):
        v = self.value()
        if not v or v == 'all':
            return queryset
        if v == 'auto':
            return queryset.filter(insurance_type__in=['osago', 'kasko', 'dsago'])
        if v == 'property':
            return queryset.filter(insurance_type='property')
        if v == 'travel':
            return queryset.filter(insurance_type='travel')
        if v == 'life':
            return queryset.filter(insurance_type='life')
        if v == 'corporate':
            return queryset.filter(user__account_type='company')
        if v == 'individual':
            return queryset.filter(user__account_type='individual')
        return queryset


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'category_label', 'insurance_type',
                    'account_type_label', 'status', 'created_at', 'user',
                    'tech_passport_preview')
    list_filter = (CategoryFilter, 'status', 'insurance_type')
    search_fields = ('full_name', 'phone', 'email', 'user__username',
                     'user__company_name')
    list_editable = ('status',)
    list_per_page = 30
    readonly_fields = ('tech_passport_preview',)
    fields = (
        'user', 'full_name', 'phone', 'email',
        'insurance_type', 'object_info',
        'tech_passport', 'tech_passport_preview',
        'comment', 'status',
    )

    @admin.display(description=_('Категория'))
    def category_label(self, obj):
        t = obj.insurance_type
        if t in ('osago', 'kasko', 'dsago'):
            return 'Авто'
        return {
            'property': 'Имущество',
            'travel': 'Путешествия',
            'life': 'Жизнь',
            'other': 'Другое',
        }.get(t, '—')

    @admin.display(description=_('Тип клиента'))
    def account_type_label(self, obj):
        if not obj.user:
            return '—'
        return 'Компания' if obj.user.account_type == 'company' else 'Физ. лицо'

    @admin.display(description=_('Техпаспорт'))
    def tech_passport_preview(self, obj):
        if not obj.tech_passport:
            return '—'
        return format_html(
            '<a href="{0}" target="_blank" rel="noopener">Открыть</a>'
            '<div><img src="{0}" style="max-height:120px;max-width:220px;border-radius:6px;margin-top:6px" /></div>',
            obj.tech_passport.url,
        )
