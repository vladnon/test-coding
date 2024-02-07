from tkinter import *
from game import *
from functools import partial


class Main:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('600x400')
        self.root.title("Игра")
        self.cost = 0
        self.value = 'Результат игры: недостаточно данных'
        self.res = Label(text=self.value, border=15)


    def paper(self):
        result = partial(Game.main('бумага', self.cost), self)
        self.res['text'] = f'Результат игры: {result}'
            
    def stone(self):
        result = partial(Game.main('камень', self.cost), self)
        self.res['text'] = f'Результат игры: {result}'

    def scissors(self):
        result = Game.main('ножницы', self.cost)
        self.res['text'] = f'Результат игры: {result}'


    def run(self):
        # stone_img = PhotoImage("/home/vlad/Documents/test-python-main/типо игра/stone.jpg")

        # stone_img.zoom(1000, 1000)

        paper_b = Button(text="Бумага", font=10, border=5, command=self.paper)
        stone_b = Button(text="Камень", border=5, font=10, command=self.stone)
        scissors_b = Button(text="Ножницы", font=10, border=5, padx=3, command=self.scissors)

        entry_cost = Entry(textvariable=self.cost)

        paper_b.grid()
        stone_b.grid()
        scissors_b.grid()

        # enemy = Label(text='----', font=100000)

        self.res.place(x=200, y=100)
        # enemy.grid(row=5, column=5)

        self.root.mainloop()
        
if __name__ == "__main__":
    main = Main()
    main.run()