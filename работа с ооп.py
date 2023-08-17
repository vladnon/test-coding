"""классы"""
# метод - это функция, которая пренадледит классу
#  класс - по суте капсуле в котором собрано все содержимое класса
# class House():
#     def __init__(self, street, number):
#         self.street = street
#         self.number = number
#         self.age = 0
        
#     def build(self):
#         print("Дом на улице " + self.street + "под номером ", str(self.number) + " построен")

#     def age_of_house(self, year):
#         self.age +=year

# House1 = House("Московская", 20)
# House2 = House("Московская", 21)
# House1.age_of_house(5)
# print(House1.age)

"""наследничество в классах, сейчас я сделал класс - потомок, а верхний класс - родитель"""

# class ProspectHouse(House):
#     def __init__(self, prospect, number):
#         self.prospect = prospect
#         super().__init__(self,number) 
# # super берет из класса родителя атребут number
# # класс-потомок берет все атрибуты и методы из класса родителя
# Prhouse = ProspectHouse("Ленина", 5)
# print(Prhouse.prospect)


"""декораторы"""
# пишутся через @ например, чтобы сделать из функции свойство класс нужен декоратор property, чтобы сделать метод класса - classmethod,  и чтобы сделать статичный метод - staticmethod

# class Cat:
#     def __init__(self, age, color, weight):
#         self.age = age
#         self.color = color
#         self.weight = weight

    # @classmethod
    # def sum_age(cls, count):
        # у  метода класса обязательным атрибутом долден быть cls

    # @staticmethod
    # def find_color():
        #  у статичного метода нет обязательного атрибута

    # @property
    # def find_weight(self):
        # у свойства как и у простых фунций атрибут self
    
    # @find_weight.setter
    # def 
    # setter - значение свовойства
    # @find_weight.getter
    # def
    # getter - возвращает значение

"""магические мотоды в классе и класс"""
# class Banknote:
#     def __init__(self, value):
#         self.value = value

#     def __repr__(self):
#         return f"Banknote({self.value})"
    
    # строка для программиста

    # def __str__(self):
    #     return f"Банкнота наминалом в {self.value} рублей"
    # # строка для пользователя
    # #  если нет какой-то метода, то питон вернет тот вариант который есть
    # def __eq__(self, other) :
    #     if other is None or not isinstance(other, Banknote):
    #         return False
    #     return self.value == other.value
    #  сравнение
    #  eq по умолчанию сравнивает адрес в памяти, в реалезации лучше сразу проверить тип

    # def __lt__(self, other):
    #     if other is None or not isinstance(other, Banknote):
    #         return False
    #     return self.value < other.value
        
    # отвечает за знак меньше 

    # def __gt__(self, other):
    #     if other is None or not isinstance(other, Banknote):
    #         return False
    #     return self.value > other.value
    
    # отвечает за знак больше
    
    # def __le__(self, other):
    #     if other is None or not isinstance(other, Banknote):
    #         return False
    #     return self.value <= other.value
    
    # отвечает за знак меньше или равно

    # def __gt__(self, other):
    #     if other is None or not isinstance(other, Banknote):
    #         return False
    #     return self.value >= other.value
    
    # отвечает за знак больше или равно

"""если этих методов не будет, то сравнение нельзя будет реализовать"""

# class Iterator:
#     def __init__(self, container):
#         self.container = container
#         self.index = 0
    
#     def __next__(self):
#         if  0 <= self.index and self.index < len(self.container):
#             value = self.container[self.index]
#             self.index += 1
#             return value
#         raise StopIteration
#     #  итератор
    #  должен вернуть следующий обьект из контейнера, кто его реализует = Итератор


# class Wallet:
#     def __init__(self, *bankotes:Banknote):
#         self.container = []
#         self.container.extend(bankotes)
#         self.index = 0

#     def __repr__(self):
#         return f"Wallet{self.container}"
    
    # def __str__(self):
    #     return f"В вашем  кошельке {self.container} денег"

    # def __contains__(self, item):
    #     return item in self.container
    #  проверки in -  например находится ли банкнота в кошельке

    # def __bool__(self):
    #     return len(self.container)>0
# как я и писал раньше проверка на тру самодельных обьектов, всегда будет тру, но чтобы это поменять например, если кошелек будет пустым, то будет фалс, надо написать этот дандер метод 

    # def __len__(self):
    #     return len(self.container)
    #  этот метод нужен чтобы измерить длину контейнера

    # def __call__(self):
    #     return f"{sum(e.value for e in self.container)} рублей"
    # чтобы обьект стал вызываемым, нужна этот метод, иначе будет ошибка

    # def __iter__(self):
    #     return Iterator(self.container)
    #  этот метод возвращает обьект итератор, в примере просто обращается к итератору, тот кто реализует итер = Итерабл

    # def __getitem__(self, item : int):
    #     if item < 0 or item > len(self.container):
    #         raise IndexError
    #     return self.container[item]
    #  принимает число, и возвращает значение по индексу, но может работать и как словарь, тоесть по ключу
    #  может работать, если нет итератора
    #  нужен для функционала [],(аналог списка и словаря)
    # def __setitem__(self, key : int, value : Banknote):
    #      if key < 0 or key > len(self.container):
    #         raise IndexError
    #      self.container[key] = value

    # нужен для присвоения через [], если не реализовать - ошибка
  

# if __name__ == "__main__":
#     banknote = Banknote(50)
#     fifty = Banknote(50)
#     hundred = Banknote(100)
#     wallet  = Wallet(fifty, hundred, hundred)
    # print(wallet)
    # print(hundred in wallet)
    # if wallet:
    #     print("ok")
    # print(len(wallet))
    # print(wallet())
    # for money in wallet:
    #     print(money)
    # #  если надо пройтись по всем обьектом контейнера, надо сделать итератор и итернабл
    #  проверка на тру самодельных обьектов, всегда будет тру
    # print(fifty >= hundred)
    # print(fifty == hundred)
    # print(banknote)
    # print(f"{banknote!r}")
    # wallet[0] = Banknote(500)
    # print(wallet[0])
    # for money in wallet:
    #     print(money)

"""Инкапсуляция"""
# суть инкапсуляции в том, что мы собираем данные и методы в одном месте - классе для работы с ними и предоставлене пользователю публичного интерфейса(API)
# _ - (protected)знак того, что этот атрибут не предназначен для прямого использования. Работа обьекта не гарантируется при работе таких атрибутов
# __ - (private) под копотом преобразуется в object._Class__attribute(только для случаев когда начиается с __)
#  публийчный АПИ(интейрфейс) - это контракт, все методы будут работать, а внутренняя реализация не будет гарантироваться
#  совет таков - делать одно _ для атрибутов и реальзаций, не перебаршивать с __ и сеттерами/геттерами
# class Person:
#     def __init__(self, first_name, last_name, age):
#             self._first__name = first_name
#             self._last_name = last_name
#             self.__age = age
            
        
#     def set_age(self, age):
#         if age < 0 and age> 120:
#             raise ValueError(f"Возраст должен быть от 1-120")
#         self.__age = age
        
        
#     def describe(self):
#             print(f"Привет, я {self._first__name} {self._last_name}, и мне {self.__age} лет")
        
        
# if __name__ == "__main__":
#     ivan = Person("Иван", "Иванов", 24)
#     ivan._age = 1000
    
#       но так любой может поменять какой - то параметр, первое что можно сделать - поставить _ в начало, второй же сделать setter
#     ivan._Person__age = 100
#      но и setter тоже можно обойти
#     ivan.describe()
#     print(ivan._Person__age)

"""Наследование"""
# Наследовние(inheritance) - механизм. получения доступа к данным и поведения своего предка И расширению(изменения поведения) классов не мення код
# Главная ошибка программиста - повторение. Так что мы должны понять что обьединяет классы и испрвить код с помощью наследования
# IS-A является(наследования) - это главное правило наследования
#  класс-предок, должен обьединять все классы-потомки, все классы-потомки должны быть являться ответвлением супер класса, например работники и менеджер 
# HAS-A содержить(композиция), такжже является важным правилом
# класс-предок содержит в себе класс-потомок, например машина и двигатель
#  чтобы использовать это правило напишу пример ниже, надо просто инициолизировать класс потомок в классе предке
#  эти правила важны, просто потому что твой код будут чаще читать чем переписывать, так что он должен быть логимным и понятным
#  если создвать секретные атрибуты через __ - то после наследования создастья другой экземпляр, который будет равен тому, что было указано в классе, который вызывается

"""Пример номер 1"""
# class Employee:
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus
        
#     def calc_bonus(self):
#         return self.salary // 100 * self.bonus
        
#     def __str__(self):
#         return f"Это {self.name}, работает {self.__class__.__name__}, также она получает {self.salary} и бонус {self.bonus}% что будет равно {self.calc_bonus()}"

# class Cleaner(Employee):
#     def __init__(self, name):
#         super().__init__(name, 10000, 5)
        
# class Manager(Employee):
#     def __init__(self, name):
#         super().__init__(name, 40000, 40)
    
# class Ceo(Employee):
#     def __init__(self, name):
#         super().__init__(name, 100000, 100)
    
#     #  но если что-то надо поменять у отдельного класса, то можно вызвать метод и переписать его как надо
#     def calc_bonus(self):
#         return 200000

# def calc_bs(employees:Employee):
#     for employee in employees:
#         print(f"Рассчитываем бонус для {employee.name}, это {employee.calc_bonus()}")
        
        
# if __name__ == "__main__":
#     masha = Cleaner("Маша")
#     print(masha)
#     ivan = Manager("Иван")
#     print(ivan)
#     sasha = Ceo("Саша")
#     print(sasha)
#     a_list = [masha, ivan, sasha]
#     calc_bs(a_list)
    
    
# """Пример номер два"""
# class Mylist(list):
#     def __str__(self):
#         return super().__str__().replace(",", ",\n")
    
# if __name__ == "__main__":
#     print(list(range(1, 4)))
#     my_list = Mylist(list(range(1, 4)))
#     print(my_list)
    # причем все функции и вызов по индесу будут работать, так как наш класс в этом примере унаследовали все у list, и по просто поменяли дандер метод __str__
#     print(my_list[1])
#     my_list.extend([4, 5])
#     print(my_list)
    
    
# class Engine:
#     pass

# class Car:
#     def __init__(self):
#         self.engine = Engine
        
#     def start(self):
#         self.engine.start()
#  кароче завтра после школы напиши код, которые на фигуры, типо класс-предок фигура, классы-потомки треугольник. квадрат и тд и сделать неизменяемый словарь

        
# class Fig():
#     def __init__(self, name):
#         self.name = name

#     def calc_square_rect(self, l_side, r_side):
#         return f"Это фигура {self.name} и ее площадь - {2 * (l_side + r_side)}"

#     def calc_square_tr(self, l_side, r_side):
#         return f"Это фигура {self.name} и ее площадь - {int((l_side * r_side) / 2)}"

# class Tr(Fig):
#     def square(self, frst_side, scnd_side):
#         return self.calc_square_tr(frst_side , scnd_side)

# class Kv(Fig):
#     def square(self, frst_side, scnd_side):
#         return self.calc_square_rect(frst_side , scnd_side)

# if __name__ == "__main__":
#     rect = Kv("прямоугольник")
#     print(rect.square(20, 20))
#     tr = Tr("треугольник")
#     print(tr.square(20, 20))
    
    


""" Полиморфизм и утиная типизация"""
# Полиморфизм -это механизм, позволяющий выполнять один и тотже код по разному
#  сначала будет пример, как полиморфизм работает в других языках с статической типизацией, а не с димнамической как в питоне
# щас чуть чуть подправлю код выше  
# смысл утиной типизации - если кто то крякает и ходит как утка, все подумают что это утка, не зависимо от того утка это или нет
#  тоесть питону не важно кто ты(что за тип обьекта),а важно что ты умеешь(поведение)
# для утиной типизации важно только наличие поведения для использования в полиморфизме
# также стоит понимать что в питоне все основано на полиморфизме(Динамическая типизация вездесуща), например я хочу создать функцию и избежать global, я просто пишу в аргументы функции полиморфный параметр, и он будет меняться взависимости от того что я туда передал, но сам код я не менял, главное чтобы у переменных было одно и того поведение
# def add(a:int, b:int):
#     return a + b


# def add(a:str, b:str):
#     return f"{a}{b}"

# def add(a:float, b:float):
#     return round(a + b, 3)

# if __name__ == "__main__":
#     print(add(1.2, 1.2))
#     #  выведет 2.4   
#     print(add(2, 2))
#     #  выведет 2
# #  но это так работает например в java
# class Animal:
#         def make_noise(self):
#             print("shhh")
    
# class Cat(Animal):
#     def make_noise(self):
#         print("meow")
        
# class Dog(Animal):
#     def make_noise(self):
#         print("gavv")
        
# class Car:
#     def make_noise(self):
#         print("brbrbr")
        
# def noise(animal):
#     return animal.make_noise()
        
# if __name__ == "__main__":
#      noise(Dog())
#     #  выведет gavv
#      noise(Cat())
     #  выведет meow
#  тоесть по сути функция одна, но она работает по разному с разными обьектами и я не менял ни разу код(что важно можно сравнить с декараторами), и не потому что они таковы, а потому что они они делают разные вещи
    #  noise(Car())
    # хоть машине не животное, но она издает звук, тоесть в питоне так можно делать ну лучше не стоит, потому что это не логично => неудобно читать
"""Другой пример который типо похож на реальную задачу(но нет)"""
# class SQLiteDataBase:
#     def connect(self):
#         print("connecting to database SQLiteDataBase")
        
#     def got_users(self):
#         print("get users with SQL")
        
# class MongoDataBase:
#     def connect(self):
#         print("connecting to database MongoDataBase")
        
#     def got_users(self):
#         print("get users with NoSQL")
        
# def get_db_from_config():
#     print("reading config")
#     return SQLiteDataBase()
        
# class Server:
#     # def get_users(self): но так будет работать только с sqlitedatabase, что щас перепишу код
#     def get_users(self, db):
#     # по сути я просто добавил полиморфную переменную
#         # db = SQLiteDataBase()
#         db.connect()
#         users = db.got_users()
#         return users
    
# def summ(a, b):
#     #  переменные a и b - полиморфные, тоесть я могу хоть str и str обьекты передать, и он не выдаст ошибку так как них одно и тоже поведение
#     return a + b 
    
# if __name__ == "__main__":
#     server = Server()
#     server.get_users(get_db_from_config())
#     print(summ("дщд", "щлы"))
    
"""Аргументы класса(classmethod и staticmethod)"""
# для примера подойдет самый простой код, чтобы не нагружать
# LEGB-rule действуют без атрибутов без приставок, например self
# если через self пытаться поменять неизменяемый атрибут(например строка), то будет создана локальная копия(у меня в классе это breed)
# если менять через self изменяемый атрибут(список), то он измениться для всех обьектов класса(у меня это список имена)
"""classmethod"""
# classmethod - нужен, чтобы работать с  атрибутами и другими методами класса
# self - ссылка на обьект, cls - ссылка на сам класс
# в методах, в которых используется self, использовать только атрибуты, которые принадлежат обьекту 
# также методы класса можно использовать, чтобы создавать конструкторы(фабрики), для создания обьектов
# главное не пытайся назвать cls self, запомни это не так работает, ты просто себя запутаешь, дело не в названии
"""staticmethod"""
# у него нет ссылок, это просто функция, связанная контекстом с классом
# нужен для простого понимания для чего нужна эта функция
# если метод не использует ссылок(self, cls), то это может быть staticmethod


# class Bluecat:
#     breed = "сейшельская"
#     names = []
#     count = 0
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.names.append(name)
        # Bluecat.breed = "другая"
        #  вот так можно поменять неизменямый атрибут через self для всех обьектов класса
#         self.inc_count()
        
#     def meow(self):
#         print(f'Кошка {self.name} породы {self.breed} мурчит в дс!')
        
#     @classmethod
#     def inc_count(cls):
#         cls.count += 1
#         # по сути cls и для ссылки и есть сам класс, ну тоесть я могу поменять breed с помощью названия класса, а могу сделать это с помощью cls
#         # вообще мы можем тоже самое прописать в __init__, но так как программирование - это про чтение кода, лучше писать так, потому что так легче читать и воспринимать код
    
#     @classmethod
#     def make_cat(cls, name):
#         if name == "Лариса":
#             return cls("Лариса", 5)
#         elif name == "Том":
#             return cls("Том", 2)
#         return cls("Бобик", 4)
#     # и тогда создание обьект, будет выглядеть намного проше, просто класс и вызвать к нему метод, в данном случае в который нужно передать имя
#     #  это удобно, когда у класса огромное количество аргументов, которые лень указывать вручную

#     """staticmethod"""
#     @staticmethod
#     def get_human_age(age):
#         # интересно, что туда ничего не передается 
#         return age * 8

# if __name__ == "__main__":
#     # larisa = Bluecat("Лариса", 5)
#     # tom  = Bluecat("Том", 2)
#     larisa = Bluecat.make_cat("Лариса")
#     # larisa.meow()
#     tom = Bluecat.make_cat("Том")
    # tom.meow()
#     # tom.breed = "другая"
#     # tom.names.append("Бобик")
#     # print(larisa.names)
#     # print(tom.names)
#     # print(Bluecat.count)
#     print(larisa.get_human_age(larisa.age))
    # надо передавать возраст обьекта, даже если мы передаем сам обьект, просто потому что у staticmethod нет ссылки на класс
    
    
"""Свойтсва и slots"""
# создам еще раз класс с котами
# сет/гет, а также свойства только при наличии логики в получении или установки атрибута
# если мы хотим добавить логику то по сути можно просто написать в __init__, но тогда ее можно поменять при вызове
# для ограничения
# __dict__ -  атрибут обьектов в питоне, который хранит в себе состояние(все что знает обьект)
# setattr вызывается при попытке установить атрибут
# setter - запретить менять атрибут или доваблять атрибут
# getter - возможность установки/получения атрибута с логикой 
# если создать setter, в init нужно запускать именно свойтво, в котором мы прописываем свой атрибут(в данном случае приватный)
# так как обьект с двумя полями занимает 350 байтов, что много нужно использовать __slots__
# __slots__ нужен для уменьшения памяти, занимемой обьектами(по сути у каждого обьекта есть свой словарь, а с слотс, все словари заменяются на кортежи, которые занимают меньше памяти)
# property - нужен чтобы расписать сеттеры и геттеры, ну и чтобы лечге читать было

# class Cat:
#     __slots__ = ("_name", "_age")
#     # по сути заменяет условие в котором нельзя добавлять новые атрибуты, да и еще меньше памяти использует, ну тоесть вообще чил
#     # а все потому что __slots__ - кортеж, тоесть во всех обьектах теперь не создается отдельный словарь, заменил все на кортеж
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Кошка (name = {self.name}, age = {self.age}) "
    
#     # def __setattr__(self, key, value):
#     #     if key not in self.Fields:
#     #         raise AttributeError(f"Только допустимы атрибуты {self.Fields}")
#     #     if key == 'name' and not value:
#     #         raise AttributeError("Имя не может быть пустым")
#     #     if key == 'age' and (value > 15 or value < 1):
#     #         raise AttributeError("Возраст кошки может быть от 0 - 15 лет")
#     #     self.__dict__[key] = value
#     # но это слишком сложно, так что на помощь приходит property(свойство)
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, value):
#         if not value:
#             raise AttributeError("Имя не может быть пустым")
#         self._name = value
        
#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, value):
#         if value > 15 or value < 1:
#             raise AttributeError("Возраст кошки может быть от 0 - 15 лет")
#         self._age = value
    
# if __name__ == "__main__":
#     angela = Cat("Анжела", 5)
#     print(angela)
    
    

    

        
    
