from tkinter import *
from game import *


def paper(event):
    result = main('бумага')
    print(result)
    
def stone(event):
    result = main('камень')
    print(result)

def scissors(event):
    result = main('ножницы')
    print(result)