"""Паттерны или шаблоны разработки"""
# Паттерны - общие способы решение частных задач и проблем
# Паттерн Singleton (Одиночка) - класс, который гарантирует, что во всей системе присутствует всего один обьект класса
# по сути метод new является настоящим конструктором, хотя init тоже так называют, но он работает уже с готовыми обьектами и инициализирует атрибуты
 # Паттерн Singleton (Одиночка) - шаблон предоставления глобального доступа к состоянию
# он нужен для одной точки доступа к данным и для того чтобы ресурсоемкие задачи сделать всего один раз
# плюсы: 1 раз выполняем тяжелые задачи, имеет один вход в систему
# минусы: обшесистемная глобальная переменная
# но один умный человек сказал, что нам же не нужен один обьект, нужно только одно и тоже состояние, так что щас напишу monostate
# модуль в питоне - это и есть singleton

# class Singleton:
#     instance = None

#     def __new__(cls):
#         if Singleton.instance == None:
#             # и так нам надо создать обьект в методе, который создает обьекты, но к нему мы не можем обратиться, т.к. это создаст рекурсия и код упадет
#             # поэтому нам нужно обратиться к классу-предку object, и уже у него вызвать метод new
#             Singleton.instance = super().__new__(cls)
#         return Singleton.instance

#     def _do_work(self):
#         print("Сделал очень сложную работу")
#         # парсинг, бд, работа с данными
#         self.data = 101

# class MonoState:
#     _shared_states = {}

#     def __init__(self):
#         self.__dict__ = self._shared_states
#         if not self._shared_states:
#             print("Сделал очень тяжелую работу")
#             self.data = 101

# if __name__ == "__main__":
#     first = MonoState()
#     # first._do_work()
#     print(first)
#     second = MonoState()
#     print(second)
#     print(first is second)
#     print(first.data)
#     first.data = 102
#     print(second.data)
#     # ну тоесть обьекты идентичны, если поменять какой либо атрибут у одного, у второго атрибут тоже поменяется
#     print(MonoState())
    # теперь обьекты разные, но состояние(данные) у них одно и тоже

"""Фабричный метод"""
# предположем у тебя есть задача сделать координаты по точке
from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESION = 1
    POLAR = 2

class Point:
    # def __init__(self, a, b , system=CoordinateSystem.CARTESION):
    #     if system == CoordinateSystem.CARTESION:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * sin(b)
    #         self.y = b * cos(b)
#  но так писать не удобно, так как после добавления новой системы координат надо снова писать логику в конструктор, да еще не понятся что на первый вгляд что есть x и что есть y(в плане a и b)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cortesian_point(x ,y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

# так теперь стало понятней читающему, атрибуты названы правильно, и менять удобно, в целом только одни плюсы

if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)
    
    
class Node:
    def __init__(self, data) -> None:
        self.data = data

