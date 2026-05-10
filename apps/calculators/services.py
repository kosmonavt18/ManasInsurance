"""
ООП в калькуляторах:

    BaseCalculator (абстрактный)
        ├── OSAGOCalculator
        ├── KASKOCalculator
        ├── PropertyCalculator
        └── TravelCalculator
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class CalculationResult:
    price: int
    currency: str = 'сом'
    breakdown: Dict[str, str] = field(default_factory=dict)


class BaseCalculator(ABC):
    name: str = 'Базовый калькулятор'

    @abstractmethod
    def calculate(self, data: dict) -> CalculationResult: ...

    @staticmethod
    def _to_int(value, default=0) -> int:
        try:
            return int(float(value))
        except (TypeError, ValueError):
            return default


class OSAGOCalculator(BaseCalculator):
    name = 'Калькулятор ОСАГО'
    BASE_TARIFF = 2500
    K_VEHICLE = {'car': 1.0, 'truck': 1.6, 'bus': 1.8, 'moto': 0.6}
    K_POWER = [(70, 0.6), (100, 1.0), (150, 1.4), (200, 1.6), (10_000, 1.9)]
    K_EXPERIENCE = [(1, 1.8), (3, 1.5), (7, 1.2), (50, 1.0)]
    K_REGION = {'bishkek': 1.3, 'osh': 1.1, 'chui': 1.0, 'other': 0.9}

    def calculate(self, data):
        vehicle = data.get('vehicle_type', 'car')
        power = self._to_int(data.get('power'), 100)
        experience = self._to_int(data.get('experience'), 5)
        region = data.get('region', 'bishkek')
        k_v = self.K_VEHICLE.get(vehicle, 1.0)
        k_p = next(k for limit, k in self.K_POWER if power <= limit)
        k_e = next(k for limit, k in self.K_EXPERIENCE if experience <= limit)
        k_r = self.K_REGION.get(region, 1.0)
        price = self.BASE_TARIFF * k_v * k_p * k_e * k_r
        return CalculationResult(int(round(price)), breakdown={
            'Базовый тариф': f'{self.BASE_TARIFF} сом',
            'К (тип ТС)': f'{k_v}', 'К (мощность)': f'{k_p}',
            'К (стаж)': f'{k_e}', 'К (регион)': f'{k_r}',
        })


class KASKOCalculator(BaseCalculator):
    name = 'Калькулятор КАСКО'
    BASE_RATE = 0.05
    K_AGE = [(3, 0.9), (7, 1.0), (12, 1.3), (50, 1.6)]
    K_EXPERIENCE = [(1, 1.5), (3, 1.2), (7, 1.0), (50, 0.9)]
    K_FRANCHISE = {'0': 1.0, '10000': 0.85, '30000': 0.7, '50000': 0.6}

    def calculate(self, data):
        car_value = self._to_int(data.get('car_value'), 0)
        car_age = self._to_int(data.get('car_age'), 5)
        experience = self._to_int(data.get('experience'), 5)
        franchise = data.get('franchise', '0')
        k_age = next(k for limit, k in self.K_AGE if car_age <= limit)
        k_exp = next(k for limit, k in self.K_EXPERIENCE if experience <= limit)
        k_fr = self.K_FRANCHISE.get(franchise, 1.0)
        price = car_value * self.BASE_RATE * k_age * k_exp * k_fr
        return CalculationResult(int(round(price)), breakdown={
            'Стоимость авто': f'{car_value} сом',
            'Базовая ставка': f'{int(self.BASE_RATE * 100)} %',
            'К (возраст авто)': f'{k_age}', 'К (стаж)': f'{k_exp}',
            'К (франшиза)': f'{k_fr}',
        })


class PropertyCalculator(BaseCalculator):
    """
    Имущество: стоимость дома × тариф.
    Умный дом    = 0.16%
    Умный дом+   = 0.20%
    """
    name = 'Калькулятор страхования имущества'
    TARIFFS = {
        'smart':      ('Умный дом',  0.0016),
        'smart_plus': ('Умный дом+', 0.0020),
    }

    def calculate(self, data):
        amount = self._to_int(data.get('amount'), 0)
        tariff_key = data.get('tariff', 'smart')
        label, rate = self.TARIFFS.get(tariff_key, self.TARIFFS['smart'])
        price = amount * rate
        return CalculationResult(int(round(price)), breakdown={
            'Стоимость дома': f'{amount} сом',
            'Тариф': f'{label} ({rate * 100:.2f}%)'.replace('.00', ''),
        })


class TravelCalculator(BaseCalculator):
    """
    Путешествия. База за 1 человека на 7 дней:
      world_us  — Весь мир (с США/Канадой): 1200 сом
      world     — Весь мир (без США/Канады): 800 сом
      schengen  — Шенгенская зона: 500 сом
    Итог = (база / 7) × дни × кол-во человек.
    """
    name = 'Калькулятор страхования путешествий'
    BASE_PER_WEEK = {
        'world_us': ('Весь мир (с США и Канадой)', 1200),
        'world':    ('Весь мир (без США и Канады)', 800),
        'schengen': ('Шенгенская зона', 500),
    }
    DAYS_CHOICES = [7, 14, 21, 31, 62, 93, 180, 270, 360]

    def calculate(self, data):
        people = max(1, self._to_int(data.get('people'), 1))
        days = self._to_int(data.get('days'), 7)
        if days not in self.DAYS_CHOICES:
            days = 7
        zone = data.get('zone', 'world')
        label, base_week = self.BASE_PER_WEEK.get(zone, self.BASE_PER_WEEK['world'])
        per_person = (base_week / 7) * days
        price = per_person * people
        return CalculationResult(int(round(price)), breakdown={
            'Зона покрытия': label,
            'Базовая ставка (7 дн / чел)': f'{base_week} сом',
            'Дней пребывания': str(days),
            'Человек': str(people),
            'На человека': f'{int(round(per_person))} сом',
        })


CALCULATORS = {
    'osago': OSAGOCalculator(),
    'kasko': KASKOCalculator(),
    'property': PropertyCalculator(),
    'travel': TravelCalculator(),
}
