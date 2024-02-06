from tkinter import *
from game import *
from buttons import *

root = Tk()


paper_b = Button(text="Бумага")
stone_b = Button(text="Камень")
scissors_b = Button(text="Ножницы")


paper_b.pack(side=LEFT)
stone_b.pack(side=RIGHT)
scissors_b.pack(side=TOP)

paper_b.bind("<Button-1>", paper)
stone_b.bind("<Button-1>", stone)
scissors_b.bind("<Button-1>", scissors)


root.mainloop()