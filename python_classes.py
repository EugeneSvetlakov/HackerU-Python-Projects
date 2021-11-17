from __future__ import annotations
# from typing import Dict


class Machine:
    def __init__(self, type: str, weigth: int, **kw) -> Machine:
        # Это конструктор, он вызывается при создании объекта
        self.type = type
        self.weigth = weigth
        super(Machine, self).__init__(**kw)

    def __str__(self) -> str:
        return f'type: {self.type}, weigth: {self.weigth}'

    def show(self) -> str:
        # Вызывается для вывода на экран всех свойств объекта
        return Machine.__str__(self)


class Fuel:
    def __init__(self, fuel_type: str, **kw):
        self.fuel_type = fuel_type
        super(Fuel, self).__init__(**kw)

    def __str__(self) -> str:
        return f'fuel_type: {self.fuel_type}'


class Car(Machine, Fuel):
    def __init__(self, type: str, weigth: int, fuel_type: str):
        super(Car, self).__init__(
            type=type, weigth=weigth, fuel_type=fuel_type)

    def __str__(self) -> str:
        return f'{super().__str__()}, fuel_type: {self.fuel_type}'

    def show(self) -> str:
        # Вызывается для вывода на экран всех свойств объекта
        return Car.__str__(self)

    def get_param_list(self) -> dict:
        return {
            "type": self.type,
            "weight": self.weigth,
            "fuel_type": self.fuel_type
        }


# Создание объектов
terrano1 = Car('Nissan Terrano1', '1800', 'бензин')
kia = Car('Kia Sportage', '2200', 'электричество')

# Теперь можно воспользоваться его внешним интерфейсом: методом show()
print(terrano1)
print(kia)
dict1 = kia.get_param_list()
print(dict1)

print(
    f'annotation for func get_param_list:'
    f' {Car.get_param_list.__annotations__}')

# Результат:
# Воробей носит одежду размера S.
# Попугай ара носит одежду размера XL и разговаривает.
# Попугай Корелла носит одежду размера S и щебечет.
