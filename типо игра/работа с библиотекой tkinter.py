from tkinter import *
from game import Game

# чтобы обозначить
root = Tk()

# название программы
root.title("Игра")
# размер окна
root.geometry('400x200')
# можно ли изменять размер
root.resizable(width=True, height=True)

# переменная, куда будет складываться весь полученный текст
value = StringVar()

# чтобы создать виджет текста
start_text = Label(text="Привет")
# чтобы создать виджет текста, который будет писать пользователь, и передать туда перменную для складывания значений в нее
e = Entry(textvariable=value)

# чтобы расположить виджет
start_text.pack(side=TOP)
# либо так
# start_text.grid(row=1, column=1)

def start(event):
    get = value.get()
    start_text['text'] = get
    
b = Button()

# по нажатию левой кнопки мыши, выполняется функция выше, нажатие кнопки enter, будет Return
b.bind('<Button-1>', start)
b.pack()

e.pack()

root.mainloop()