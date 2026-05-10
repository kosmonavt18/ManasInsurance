from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('full_name', 'phone', 'email', 'insurance_type',
                  'object_info', 'tech_passport', 'comment')
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned = super().clean()
        itype = cleaned.get('insurance_type')
        if itype in Application.AUTO_TYPES and not cleaned.get('tech_passport'):
            self.add_error('tech_passport',
                           'Для автострахования необходимо приложить фото тех. паспорта.')
        return cleaned
