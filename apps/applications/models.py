from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel


class Application(TimeStampedModel):
    INSURANCE_TYPE_CHOICES = [
        ('osago', 'ОСАГО'),
        ('kasko', 'КАСКО'),
        ('dsago', 'ДСАГО'),
        ('life', 'Страхование жизни'),
        ('travel', 'Страхование путешествий'),
        ('property', 'Имущество'),
        ('other', 'Другое'),
    ]
    AUTO_TYPES = {'osago', 'kasko', 'dsago'}

    STATUS_CHOICES = [
        ('pending', 'Ожидает проверки'),
        ('approved', 'Подтверждено'),
        ('rejected', 'Отклонено'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='applications',
                             verbose_name=_('Клиент'))
    full_name = models.CharField(_('ФИО / Компания'), max_length=200)
    phone = models.CharField(_('Телефон'), max_length=40)
    email = models.EmailField(_('Email'), blank=True)
    insurance_type = models.CharField(_('Тип страхования'), max_length=20,
                                      choices=INSURANCE_TYPE_CHOICES)
    object_info = models.CharField(_('Что страхуем'), max_length=200,
                                   help_text='Например: Toyota Camry 2020, или путешествие в Турцию')
    tech_passport = models.ImageField(
        _('Тех. паспорт (для авто)'), upload_to='tech_passports/',
        blank=True, null=True,
        help_text='Загрузите фото тех. паспорта при автостраховании.'
    )
    comment = models.TextField(_('Комментарий'), blank=True)
    status = models.CharField(_('Статус'), max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки')

    def __str__(self):
        return f'#{self.pk} {self.full_name} — {self.get_insurance_type_display()} ({self.get_status_display()})'

    @property
    def status_color(self) -> str:
        return {'pending': 'warning', 'approved': 'success', 'rejected': 'danger'}.get(self.status, 'muted')
