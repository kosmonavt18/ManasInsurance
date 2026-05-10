"""ООП: ClientProduct наследуется от абстрактного BaseInsuranceProduct."""
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.insurance_base import BaseInsuranceProduct


class ClientProduct(BaseInsuranceProduct):
    """Продукт для частных клиентов: жизнь, путешествия и т.д."""
    KIND_CHOICES = [
        ('life', _('Страхование жизни')),
        ('travel', _('Страхование путешествий')),
        ('health', _('Медицинское страхование')),
        ('property', _('Страхование имущества')),
    ]
    kind = models.CharField(_('Вид'), max_length=20, choices=KIND_CHOICES, default='life')

    class Meta:
        verbose_name = _('Продукт для частных клиентов')
        verbose_name_plural = _('Продукты для частных клиентов')

    # переопределяем полиморфные методы
    def get_short_info(self) -> str:
        return f'{self.get_kind_display()}: {self.short_description} (от {self.price_from} сом)'

    def get_category_label(self) -> str:
        return 'Частным клиентам'
