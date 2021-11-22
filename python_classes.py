from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

# Data Classes (need 'from dataclasses import dataclass')


@dataclass
class Point:
    x: int
    y: int
    z: any


@dataclass
class Addr:
    city: str
    street: str
    flat: int


@dataclass
class ClassWithFieldAnnotatedByClassPoint:
    mylist: list[Point]
    t: int = 20


@dataclass
class ICombi:
    # def __str__(self) -> str:
    #     return super().__str__()

    def i_func(self, param1: str, param2: str) -> list:
        return [param1, param2]


@dataclass
class Combi(Addr, Point, ICombi):
    def combi_cl_func(self, param1: int, param2: str):
        pass


class Machine:
    def __init__(self, type: str, weigth: int, **kw) -> Machine:
        # Это конструктор, он вызывается при создании объекта
        self.type = type
        self.weigth = weigth
        # super(Machine, self).__init__(**kw)

    def __str__(self) -> str:
        return f'type: {self.type}, weigth: {self.weigth}'

    def show(self) -> str:
        # Вызывается для вывода на экран всех свойств объекта
        return Machine.__str__(self)


class Fuel:
    def __init__(self, fuel_type: str, **kw) -> Fuel:
        self.fuel_type = fuel_type
        # super(Fuel, self).__init__(**kw)

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


# работа с dataclass
sempl1 = Combi(x=1, y=2, z=1, city="J-Ola", street="Petrov st.", flat=44)
res1 = sempl1.i_func("aa", "aa")
print()
print(f"Repr of Combi class: {sempl1.__repr__()}")
print(f"__str__ of Combi: {sempl1}")
print()

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
# 'type: Nissan Terrano1, weigth: 1800, fuel_type: бензин'
# 'type: Kia Sportage, weigth: 2200, fuel_type: электричество'
# '{'type': 'Kia Sportage', 'weight': '2200', 'fuel_type': 'электричество'}'
# 'annotation for func get_param_list: {'return': 'dict'}'

print("sd", "sdaa")


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: Optional[str]
    duration: float
    distance: float
    speed: float
    calories: float

    MESSAGE: str = ('Тип тренировки: {training_type}; '
                    'Длительность: {duration:.3f} ч.; '
                    'Дистанция: {distance:.3f} км; '
                    'Ср. скорость: {speed:.3f} км/ч; '
                    'Потрачено ккал: {calories:.3f}.'
                    )

    def get_message(self) -> str:
        """
        Возвращает форматированную строку
        с описание и параметрами тренировки
        """
        return self.MESSAGE.format(training_type=self.training_type,
                                   duration=self.duration,
                                   distance=self.distance,
                                   speed=self.speed, calories=self.calories)
