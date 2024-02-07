from tkinter import *
from game import *

root = Tk()

root.geometry('600x400')

value = StringVar()

def paper(event):
    result = main('бумага')
    res['text'] = result
    
def stone(event):
    result = main('камень')
    res['text'] = result

def scissors(event):
    result = main('ножницы')
    res['text'] = result

# stone_img = PhotoImage("C:/Users/213-4/Documents/test-python-main/типо игра/img/png-transparent-video-game-stones-and-rocks-miscellaneous-game-video-game.png")

paper_b = Button(text="Бумага", font=10)
stone_b = Button(text="Камень", font=10)
scissors_b = Button(text="Ножницы", font=10)


paper_b.grid()
stone_b.grid()
scissors_b.grid()

res = Label(text=value, font=100000, border=10)
# enemy = Label(text='----', font=100000)

res.grid(sticky=N, row=10, column=10)
# enemy.grid(row=5, column=5)

paper_b.bind("<Button-1>", paper)
stone_b.bind("<Button-1>", stone)
scissors_b.bind("<Button-1>", scissors)


root.mainloop()