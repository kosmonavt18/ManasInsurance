from django import forms


class OSAGOForm(forms.Form):
    VEHICLE_CHOICES = [('car', 'Легковой'), ('truck', 'Грузовой'),
                       ('bus', 'Автобус'), ('moto', 'Мотоцикл')]
    REGION_CHOICES = [('bishkek', 'Бишкек'), ('osh', 'Ош'),
                      ('chui', 'Чуйская обл.'), ('other', 'Другие регионы')]
    vehicle_type = forms.ChoiceField(label='Тип ТС', choices=VEHICLE_CHOICES)
    power = forms.IntegerField(label='Мощность, л.с.', min_value=10, max_value=1000, initial=100)
    experience = forms.IntegerField(label='Стаж, лет', min_value=0, max_value=70, initial=5)
    region = forms.ChoiceField(label='Регион', choices=REGION_CHOICES)


class KASKOForm(forms.Form):
    FRANCHISE_CHOICES = [('0', 'Без франшизы'), ('10000', '10 000 сом'),
                         ('30000', '30 000 сом'), ('50000', '50 000 сом')]
    car_value = forms.IntegerField(label='Стоимость авто, сом', min_value=50_000)
    car_age = forms.IntegerField(label='Возраст авто, лет', min_value=0, max_value=40, initial=3)
    experience = forms.IntegerField(label='Стаж водителя, лет', min_value=0, max_value=70, initial=5)
    franchise = forms.ChoiceField(label='Франшиза', choices=FRANCHISE_CHOICES)


class PropertyForm(forms.Form):
    TARIFF_CHOICES = [
        ('smart', 'Умный дом (0.16%)'),
        ('smart_plus', 'Умный дом+ (0.20%)'),
    ]
    amount = forms.IntegerField(label='Стоимость дома, сом', min_value=10_000)
    tariff = forms.ChoiceField(label='Тариф', choices=TARIFF_CHOICES, widget=forms.RadioSelect, initial='smart')


class TravelForm(forms.Form):
    ZONE_CHOICES = [
        ('world_us', 'Весь мир (с США и Канадой)'),
        ('world',    'Весь мир (без США и Канады)'),
        ('schengen', 'Шенгенская зона'),
    ]
    DAYS_CHOICES = [(d, f'{d} дней') for d in (7, 14, 21, 31, 62, 93, 180, 270, 360)]
    people = forms.IntegerField(label='Количество человек', min_value=1, max_value=50, initial=1)
    days = forms.TypedChoiceField(label='Максимальный срок пребывания',
                                  choices=DAYS_CHOICES, coerce=int, initial=7)
    zone = forms.ChoiceField(label='Зона покрытия', choices=ZONE_CHOICES, initial='world')
