from tkinter import *
from game import *
from buttons import *

root = Tk()

root.geometry('600x400')


def paper(event):
    result = main('бумага')
    res['text'] = result
    
def stone(event):
    result = main('камень')
    res['text'] = result

def scissors(event):
    result = main('ножницы')
    res['text'] = result



paper_b = Button(text="Бумага", font=10)
stone_b = Button(text="Камень", font=10)
scissors_b = Button(text="Ножницы", font=10)


paper_b.grid(row=5, column=10)
stone_b.grid(row=10, column=15)
scissors_b.grid(row=15, column=20)

res = Label(text='-------', font=100000)
# enemy = Label(text='----', font=100000)

res.grid(sticky=N)
# enemy.grid(row=5, column=5)

paper_b.bind("<Button-1>", paper)
stone_b.bind("<Button-1>", stone)
scissors_b.bind("<Button-1>", scissors)


root.mainloop()