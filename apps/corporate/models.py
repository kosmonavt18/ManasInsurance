"""ООП: CorporateProduct тоже наследуется от BaseInsuranceProduct."""
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.insurance_base import BaseInsuranceProduct


class CorporateProduct(BaseInsuranceProduct):
    KIND_CHOICES = [
        ('property', _('Имущество компаний')),
        ('dms', _('Добровольное медицинское страхование')),
        ('bank', _('Страхование банковской деятельности')),
        ('liability', _('Обязательные виды страхования гражданской ответственности')),
    ]
    kind = models.CharField(_('Вид'), max_length=20, choices=KIND_CHOICES, default='property')

    class Meta:
        verbose_name = _('Корпоративный продукт')
        verbose_name_plural = _('Корпоративные продукты')

    def get_short_info(self) -> str:
        return f'[Корп.] {self.get_kind_display()}: {self.short_description}'

    def get_category_label(self) -> str:
        return 'Корпоративным клиентам'
