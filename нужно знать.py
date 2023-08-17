"""тернарный оператор и выражение"""
#  нужен для упрощения кода, например есть условие, после выполнения которого будет задано определенное значения для переменной
# nums = list(range(6))
# num = 5 if len(nums) == 6 else 7
# print(num)
# num = 5 
# print("True" if num == 5 else "False")

"""else с циклами """
#  else можно ставить в for и while, но else будет выполнятся только после успешного выполнения
# nums = list(range(6))
# for items in nums:
#     print(items)
# else:
#     print("Ну все короче")
#  также else может использоваться вместе с try и except

""" *args и **kwarks""" 
# предположем у нас есть фунция, которая сумирует все числа которые в нее попадают. Но атрибутов в этом случае должно быть такое кол-во как и чисел. В этом поможет *args
# def sum1(*args):
#     print(sum(args))
# sum1(20, 3 ,4, 90)
#  также у функции можно задать атрибут по умолчанию
# def func(x, y, z = "z"):
#     print(z)
# func(1, 2, "y")
#  **kwarks - то же самое что и *args, только возвращает словарь
"""Listcomps и genexp"""
# List comprehesion - listcomps
# Generator expression - genexp
#  они строются по типу [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# также важно понимать, что переменные доступны только внутри выражений, но в цикле так можно сделать, и переменная будет равна последнему элементу
#  можно и делать и два цикла, ну например перебрать сначала слова в текста, а потом буквы в словах
# в таких случаях, важен порядок циклов, так как интерпритатор читает код также как и мы(слева направо)
# генератор проверяет источник при создании, если источник нельзя перебирать, то будет ошибка
# генератор одноразовый, тоесть после того как но себя исчерпает, он умрет, и при вызове его будет ошибка StopItterration
# from time import sleep
# import pprint

# squares = [e ** 2 for e in range(10) if e % 2 == 0]
# # выведет четные числа от 0 до 10 и возведет их во вторую степень
# # фильтруем и преобразуем

# text = "hello world!"
# words = [word.capitalize () for word in text.split()]
# # разделяет текст на слова(по пробелам), и выводит эти слова с большой буквы
# # только преобразовываем

# nums = [-1, -2, -3, 0, 1, 5]
# positives = [ e for e in nums if e > 0 ]
# # выводит только положительные числа из списка
# # только фильтруем
# # хотя по сути только фильтровать фильтровать и только преобразовывать с помощью lambda, но нельзя делать и то и то вместе
# positives_ = list(filter(lambda e: e > 0, nums))
 
# letters = [letters for word in text.split() for letters in word if letters < "l"]
# # выведет все буквы до l

# matrix = [list(range(x, x + 3)) for x in range(3)]

# #  также можно работать и с сетом, что бы например сделать все числа уникальными, просто нужно взять в скобки
# uniqe_letters = {letter for word in text.split() for letter in word if letter < "o"}

# # и со словарями, нужно указать КЛЮЧ:ЗНАЧЕНИЕ
# alphabet = {index : letter for index, letter in enumerate("jadsklfjasodifhj")}
# """Все это были listcomps, теперь разберу генераторы"""
# #  тоже самое, но только скобки разные
# #  и еще создается обьект генератор, тоест он будет вести себя также как и в функции генератор
# positives_gen = ( e for e in nums if e > 0)
# nums_gen = (e for e in range(10))
# # мне лень писать, кароче подробнее в модуле, функция и там где функция генератор, по сути genexp тоже самое, только урезанно  


# def some_sourse():
#     print("!!!!")
#     sleep(3)
#     return  [1 ,2 ,3]

# if __name__ == "__main__":
    # print(squares)
    # print(words)
    # print(positives)
    # print(positives_)
    # print(letters)
    # pprint.pprint(matrix, indent=1, width=15)
    # print(uniqe_letters)
    # print(alphabet)
    # щас просто могу перевернуть словарь, и мне ничего не будет, ок да 
    # print({value: key for key, value in alphabet.items()})
    # print(positives_gen)
    # print(next(positives_gen))
    # #  выведет первый элемент списка
    # # чтобы вывести все элементы нужно написать цикл for
    # for item in positives_gen:
    #     print(item)
    # for num in nums:
    #     print(next(nums_gen))
        # print(next(nums_gen)) 
    # gen  = (e for e in some_sourse())    
    # мы даже еще ничего не вызвали, а он сразу же выводит восклицательные знаки
    
"""Принципы написания кода"""
#DRY - dont repeat yourself - не повторяйся
#  у нас есть две функции, которые по сути делают одно и тоже, читают файл, но разные
# принцип нам говрит не повторяться, так что выносим обшее в отдельную функцию, и в первых двух функция возравращаем 3 функцию, с атрибутами ввиде этих файлов
# и кода стало меньше, и читать легче, и еще раньше создавалось было две папки с этими файлами, а теперь только один 
# упрощает откладку и поиск ошибок


def func():
    return read_from_file("test.txt")

def func():
    return read_from_file("test2.txt")

def read_from_file(name):
    with open(f"folder/{name}") as file:
        result = file.readline()
    return result

def read_from_file(name):
    with open(f"folder/{name}") as file:
        result = file.readline()
    return result



#YAGNI - You arent gonna need it - тебе это не понадобиться
# надо понимать надо это или просто не кому не нужно
# по сути метод scratch не кому не нужен, 
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def make_meow(self):
        print(f"Кот под именем {self.name} мурчит в дс")

    def scratch(self):
        pass

#KISS - Keeo it simple, stupid - будет проще
#по сути ты можешь сделать решение задачи в 10 раз сложное, и думать что это классное решение
# но код чаще читают, чем пишут, так что решения должны быть проще, мол всем похер что ты знаешь, сложную тему, просто реши задачу, чтобы было понятно читающему
#POLA - pricnseple of least astonishement - не удивляй пользователя(тот кто будет читать твой  код)


#EAFP - Easier to ask for forgiveness than permission - легче извиниться, чем просить разрешения(сначала действуй) - это подход писюнца на питоне


#LBYL - look before you leap - смотри прежде чем прыгнуть(сначала спроси)
from pathlib import Path

def func():
    return read_from_file_eafp("test.txt")

def func():
    return read_from_file_lbyl("test2.txt")

# подход питониста
def read_from_file_eafp(name):
    try:
        with open(f"folder/{name}") as file:
            result = file.readline()
        return result
    except:
        # сорян
        pass

def read_from_file_lbyl(name):
    if Path(f"folder/{name}").exsists:
        with open(f"folder/{name}") as file:
            result = file.readline()
        return result
    else:
        # code
        pass



