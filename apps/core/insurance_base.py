"""
ООП: иерархия страховых продуктов.
Базовый абстрактный класс BaseInsuranceProduct и его наследники.
Используется в приложениях clients / corporate / auto.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from .models import TimeStampedModel


class BaseInsuranceProduct(TimeStampedModel):
    """
    Абстрактный базовый класс страхового продукта.
    Полиморфный метод get_short_info() переопределяется в наследниках.
    """
    title = models.CharField(_('Название'), max_length=200)
    slug = models.SlugField(_('URL-имя'), max_length=200, unique=True)
    short_description = models.CharField(_('Краткое описание'), max_length=300)
    full_description = models.TextField(_('Полное описание'))
    image = models.ImageField(_('Изображение'), upload_to='products/', blank=True, null=True)
    price_from = models.PositiveIntegerField(_('Цена от, сом'), default=0)
    is_active = models.BooleanField(_('Активно'), default=True)

    class Meta:
        abstract = True
        ordering = ['title']

    def __str__(self):
        return self.title

    # Полиморфный метод — переопределяется в наследниках
    def get_short_info(self) -> str:
        return f'{self.title} — от {self.price_from} сом'

    def get_category_label(self) -> str:
        """Каждый наследник возвращает свою метку категории."""
        return 'Страхование'
