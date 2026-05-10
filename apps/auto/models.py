"""ООП: AutoProduct + дочерние модели тарифов (таблицы цен как на скриншоте)."""
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.insurance_base import BaseInsuranceProduct
from apps.core.models import TimeStampedModel


class AutoProduct(BaseInsuranceProduct):
    KIND_CHOICES = [
        ('osago', 'ОСАГО'),
        ('kasko', 'КАСКО'),
        ('dsago', 'ДСАГО'),
        ('accident', 'Страхование от несчастного случая'),
    ]
    kind = models.CharField(_('Вид'), max_length=20, choices=KIND_CHOICES, unique=True)
    has_calculator = models.BooleanField(_('Есть калькулятор'), default=False)

    class Meta:
        verbose_name = _('Автопродукт')
        verbose_name_plural = _('Автопродукты')

    def get_short_info(self) -> str:
        return f'{self.get_kind_display()} — {self.short_description}'

    def get_category_label(self) -> str:
        return 'Автострахование'


class TariffRow(TimeStampedModel):
    """Строка таблицы цен на странице автопродукта."""
    product = models.ForeignKey(AutoProduct, on_delete=models.CASCADE, related_name='tariffs')
    label = models.CharField(_('Параметр'), max_length=200)
    value = models.CharField(_('Значение / цена'), max_length=200)
    order = models.PositiveSmallIntegerField(_('Порядок'), default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('Тариф (строка)')
        verbose_name_plural = _('Тарифы (строки)')

    def __str__(self):
        return f'{self.product.title} — {self.label}'
