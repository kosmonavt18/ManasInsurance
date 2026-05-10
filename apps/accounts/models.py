"""
Расширенная модель пользователя через наследование от AbstractUser (ООП).
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ACCOUNT_TYPE_CHOICES = [
        ('individual', _('Физическое лицо')),
        ('company', _('Компания')),
    ]
    phone = models.CharField(_('Телефон'), max_length=40, blank=True)
    middle_name = models.CharField(_('Отчество'), max_length=80, blank=True)
    account_type = models.CharField(
        _('Тип аккаунта'), max_length=20,
        choices=ACCOUNT_TYPE_CHOICES, default='individual'
    )
    company_name = models.CharField(_('Название компании'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def get_full_name(self) -> str:
        if self.account_type == 'company' and self.company_name:
            return self.company_name
        parts = [self.last_name, self.first_name, self.middle_name]
        return ' '.join(p for p in parts if p) or self.username

    @property
    def role_label(self) -> str:
        if self.is_superuser:
            return 'Администратор'
        if self.is_staff:
            return 'Сотрудник'
        return 'Клиент'

    @property
    def account_type_label(self) -> str:
        return dict(self.ACCOUNT_TYPE_CHOICES).get(self.account_type, '—')


class ClientPolicy(models.Model):
    POLICY_TYPES = [
        ('auto', 'Авто'),
        ('life', 'Жизнь'),
        ('travel', 'Путешествия'),
        ('home', 'Имущество'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='policies',
                             verbose_name=_('Клиент'))
    policy_type = models.CharField(_('Тип страховки'), max_length=20, choices=POLICY_TYPES)
    object_info = models.CharField(_('Объект'), max_length=200)
    start_date = models.DateField(_('Действует с'))
    end_date = models.DateField(_('Действует до'))
    price = models.PositiveIntegerField(_('Стоимость, сом'))

    class Meta:
        verbose_name = _('Полис клиента')
        verbose_name_plural = _('Полисы клиентов')
        ordering = ['-end_date']

    def __str__(self):
        return f'{self.get_policy_type_display()} — {self.object_info}'
