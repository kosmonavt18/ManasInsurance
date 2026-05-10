from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', max_length=80, required=False)
    last_name = forms.CharField(label='Фамилия', max_length=80, required=False)
    phone = forms.CharField(label='Телефон', max_length=40)
    email = forms.EmailField(label='Email')
    account_type = forms.ChoiceField(
        label='Регистрируюсь как',
        choices=User.ACCOUNT_TYPE_CHOICES,
        widget=forms.RadioSelect,
        initial='individual',
    )
    company_name = forms.CharField(label='Название компании', max_length=200, required=False)

    class Meta:
        model = User
        fields = ('username', 'account_type', 'company_name',
                  'first_name', 'last_name', 'phone', 'email',
                  'password1', 'password2')

    def clean(self):
        cleaned = super().clean()
        acc = cleaned.get('account_type')
        if acc == 'company' and not cleaned.get('company_name'):
            self.add_error('company_name', 'Укажите название компании')
        if acc == 'individual':
            if not cleaned.get('first_name'):
                self.add_error('first_name', 'Укажите имя')
            if not cleaned.get('last_name'):
                self.add_error('last_name', 'Укажите фамилию')
        return cleaned
