"""Декараторы"""
#  функция - полноправный обьект
#  внутренняя функция, может захватывать переменные из внешней
#  декаратор - по сути обертка функции, с помощью которой мы может ее менять, с процессе функция заменяется на внутренню функцию, в данном случае - wrapper
#  по сути декаратор можно заменить на summ = logger(summ)

# def logger(func):
#     def wrapper(*args):
#         print(f"{func.__name__} is working...")
#         print(f"{func.__name__} finished")
#         return func(*args)
#     return wrapper
        
# @logger
# def summ(a, b):
#     return a + b


# sumn = logger(summ)
# print(sumn(2, 3))
# print(summ(2 , 3))

#  кароче пишу свой декаратор
# i = int(input())
# g = int(input())

# def change(func):
#     def wrapper(*args):
#         nums = []
#         nums.extend(args)
#         print(f"Функция {func.__name__} должна вывести что все норм и ты гений ну или же {sum(nums)}")
#     return wrapper

# @change
# def list1(*args):
#     nums = []
#     nums.extend(args)
#     print(nums)

# if __name__ == "__main__":
#     list1(i, g)
    

"""Замыкания"""
# замыкание - внутрення фунция, которая  возвращается из внешней захватывает(замыкает) переменные из внешнего скоупа
# каждое замыкание хранит свое состояние(данные),они не пересекаются
#  хранит состояние(данные), предостовляет интерфейс для работы с ними, "скрывет данные", помогает избежать global
#  чтобы поменять переменныю, нужно обратиться к экземпляру функции, и использовать метод __closure__, что и есть в переводе замыкание

# def names():
#     names = []
    
#     def inner(name : str) -> list:
#         names.append(name)
#         return names
#     return inner

# def counter():
#     count = 0
    
#     def inner(value: int)-> int:
#         nonlocal count
#         count += value
#         return  count
#     return inner

# def pow_(base):
#     def inner(value):
#         return value ** base
#     return inner

# def pow_(base):
#     return lambda value: value ** base
# это тоже будет замыканием, так как lambda-функция - анонимная функция

# if __name__ == "__main__":
#     p = pow_(2)
#     print(p(5))
    # boys = names()
    # boys("Vasya")
    # print(boys.__closure__[0].cell_contents )
    # pow = pow_(2)
    # pow__ = pow_(3)
    # print(pow(5))
    # print(pow(7))
    # print(pow(9))
    # print(pow__(5))
    # print(pow__(7))
    # print(pow__(9))
    
    # count = counter()
    # print(count(1))
    # print(count(1))
    # print(count(1))
    # print(count(-3))
    # 1
    # 2
    # 3
    # 0
    # boys = names()
    # girls = names()
    # print(boys("Vlad"))
    # print(boys("Stepan"))
    # print(boys("Gena"))
    # print(girls("Elena"))
    # print(girls("Olya"))
    # print(girls("Sveta"))
    # ['Vlad']
    # ['Vlad', 'Stepan']
    # ['Vlad', 'Stepan', 'Gena']
    # ['Elena']
    # ['Elena', 'Olya']
    # ['Elena', 'Olya', 'Sveta']
    
"""генераторы"""
#  выгода генератора от простой функции
#  генератор отстонавливает на yeild, тоесть можно передлать другое значение, даже после завершение функции, а просто функция после return удаляется
#  также то что остается, это выгодня для атрубутом и переменных, так как генератор их запомнит
#  генератор не будет выводит что-то кроме обьекта-генератора, но если вывести с помощью next(), тоесть с пинком, то сможет вывести первое значение
#  в него можно написать больше условий чем в переменную squares
# squares = (e ** 2 for e in range(0, 11, 2))
# for i in squares:
#     print(i)
    

# def squares2():
#     print("generator working...")
#     for e in range(0, 11, 2):
#         yield e ** 2
"""То, что опредляет эту функцию как функцию-генератор"""
# gen = squares2()
# print(next(gen))
#  выведет с помощью next - только строку и 0, тоесть не выведет все числая
# for e in gen:
#     print(e)
# for e in gen:
#     print(e)
# for e in gen:
#     print(e)
#  генератор одноразовый, тоесть его после того как он прошлеся по всему что было, и все вывел, его нельзя запустить еще раз, иначе StopIteration

# def pause():
#     print("generator working...")
#     while True:
#         print(a)
#         yield a 
# a  = 10
# gen1 =  pause()
# print(gen1)
# print(next(gen1))
# a = 20
# print(next(gen1))

"""Аргументы по умолчанию"""
# у всех встроеннных есть аргументы по умолчанию
# например у prtin() - end = "\n", но их можно менять
# важно, что интерпритатор один раз возвращается к аргументу только один раз, тоесть если есть функция как в примере, результат на выводе будет один и тотже
# from time import time, sleep
# def print_n_times(value:str, n:int=10):
#     for _ in range(n):
#         print(value)
        
# def some_function(func):
#     print(f"Функция {func.__name__} вызвана")
#     return 1
        
# # def calc(time_= some_function(some_function)):
# #     print(time_)

# # def calc(time_ = []):
# #     time_.append(1)
# #     return time_
# # чтобы обойти ниже описанную проблему, нужно сделать такие действия
# def calc(time_ = None):
# # в аргументах по умолчанию нельзя использовать изменяемые типы данных(словари, списки, сеты)
#     if time_ is None:
#         time_ = []
#     time_.append(1)
#     return time_
# # и даже если что то передать поведение останется прежним

# if __name__ == "__main__":
#     # print_n_times("Hello world")
#     # print(1, end=',')
#     # calc()
#     # calc()
#     # sleep(2)
#     # calc()
#     # calc()
#     print(calc([]))
#     print(calc([]))
#     print(calc([]))
# вроде все нормально(выводтся во всех случаях 1), но если не передать аргумент, то появляется проблема каждый раз будет добавляться по 1 в список, так как список был создан 1 раз, и не был передан снова
# print(calc())
# print(calc())
# print(calc())
# текст был выведет только один раз, это доказывает утвеждение выше, хотя 1 было напечатано 5 раз 



