"""
Базовые модели проекта. ООП: абстрактный класс TimeStampedModel,
от которого наследуются все остальные модели сайта.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """Абстрактная модель: добавляет created_at / updated_at всем наследникам."""
    created_at = models.DateTimeField(_('Создано'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Обновлено'), auto_now=True)

    class Meta:
        abstract = True


class SiteSettings(TimeStampedModel):
    """Настройки сайта: меняются админом из /admin/. Singleton-подобная модель."""
    company_name = models.CharField(_('Название компании'), max_length=120, default='ManasInsurance')
    hero_title = models.CharField(_('Заголовок героя'), max_length=200,
                                  default='Будь под надёжной защитой')
    hero_subtitle = models.CharField(_('Подзаголовок'), max_length=300,
                                     default='Страхование жизни, авто, имущества и путешествий по всему Кыргызстану')
    phone = models.CharField(_('Телефон'), max_length=40, default='+996 (312) 00-00-00')
    email = models.EmailField(_('Email'), default='info@manasinsurance.kg')
    address = models.CharField(_('Адрес'), max_length=200, default='г. Бишкек, Джал')
    about_short = models.TextField(_('Кто мы (кратко)'),
                                   default='ManasInsurance — современное страховое агентство Кыргызстана. '
                                           'Защищаем то, что важно: вашу жизнь, семью, авто и бизнес.')
    about_full = models.TextField(_('О нас подробно'),
                                  default='Компания ManasInsurance работает на рынке страхования с 2010 года. '
                                          'За это время мы помогли более 50 000 клиентам по всей стране.')

    class Meta:
        verbose_name = _('Настройки сайта')
        verbose_name_plural = _('Настройки сайта')

    def __str__(self):
        return self.company_name

    @classmethod
    def load(cls):
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj


class InsuranceCase(TimeStampedModel):
    """Информация о страховом случае: что делать в каждой ситуации."""
    CATEGORY_CHOICES = [
        ('auto', _('Автострахование')),
        ('life', _('Жизнь')),
        ('home', _('Имущество / дом')),
        ('travel', _('Путешествия')),
    ]
    category = models.CharField(_('Категория'), max_length=20, choices=CATEGORY_CHOICES, unique=True)
    title = models.CharField(_('Заголовок'), max_length=200)
    description = models.TextField(_('Что нужно делать'))
    phone_to_call = models.CharField(_('Телефон для звонка'), max_length=40, blank=True)

    class Meta:
        verbose_name = _('Страховой случай')
        verbose_name_plural = _('Страховые случаи')

    def __str__(self):
        return f'{self.get_category_display()} — {self.title}'


class Branch(TimeStampedModel):
    """Филиал на странице контактов."""
    city = models.CharField(_('Город'), max_length=80)
    address = models.CharField(_('Адрес'), max_length=200)
    phone = models.CharField(_('Телефон'), max_length=40)
    email = models.EmailField(_('Email'), blank=True)
    map_link = models.URLField(_('Ссылка на карту'), blank=True)

    class Meta:
        verbose_name = _('Филиал')
        verbose_name_plural = _('Филиалы')

    def __str__(self):
        return f'{self.city} — {self.address}'
