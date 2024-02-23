from customtkinter import *
import tkinter
from game import *
from PIL import Image


class WindowGame:
    def __init__(self) -> None:
        # настройка окна
        self.window = CTkToplevel()
        self.window.geometry('700x500')
        self.window.title("Игра")
        self.window._set_appearance_mode('dark')
        self.window.resizable(width=False, height=False)
        self.user = Game()
        
        # создание изображение
        self.paper_img = CTkImage(light_image = Image.open('./типо игра/img/paper.png'), size=(125, 91))
        self.stone_img = CTkImage(light_image = Image.open('./типо игра/img/stone.png'), size=(130, 91))
        self.scissors_img = CTkImage(light_image = Image.open('./типо игра/img//scissors.png'), size=(87, 91))
        
        # создание кнопок
        self.paper_b = CTkButton(self.window, image=self.paper_img,  command=self.paper, text=None, fg_color="transparent", hover=False, bg_color="transparent")
        self.stone_b = CTkButton(self.window, text=None,  command=self.stone, fg_color='transparent', image=self.stone_img, hover=False)
        self.scissors_b = CTkButton(self.window, text=None,  command=self.scissors, image=self.scissors_img, fg_color='transparent', hover=False)

        # создание заголовков и прочего
        self.balance = CTkLabel(self.window, font=CTkFont(family='Benzin-Bold', size=15), text=f'Баланс: {self.user.coins}')
        self.user_sign = CTkLabel(self.window ,image=self.paper_img, text=None)
        self.enemy_sign= CTkLabel(self.window ,image=self.paper_img, text=None)
        self.res = CTkLabel(self.window, text= 'Нет',  font=CTkFont(family='Benzin-Bold', size=15), anchor=CENTER)
        self.bet_entry = CTkEntry(self.window, placeholder_text='Ставка', font=CTkFont(family='Benzin-Bold', size=10), text_color='white', width=80)


        
    # вот это полное дерьмо типо, ну просто шлак реально
    def list_int(self, nums) -> int:
        result = 0
        for num in nums:
            result += num
        return result
    
    # выглядит, как костыль серьезно
    def choose_enemy_sign(self, enemy):
        if enemy == 'бумага':
            self.enemy_sign.configure(image=self.paper_img)
        if enemy == 'камень':
            self.enemy_sign.configure(image=self.stone_img)
        if enemy == "ножницы":
            self.enemy_sign.configure(image=self.scissors_img)
       
    def paper(self):
        bet = int(self.bet_entry.get())

        self.main(self.user.main('бумага', bet))
        
            
    def stone(self):
        bet = int(self.bet_entry.get())

        self.main(self.user.main('камень', bet))
        

    def scissors(self):
        bet = int(self.bet_entry.get())

        self.main(self.user.main('ножницы', bet))
        

    def main(self, result):
        if result[0] == 'Недостаточно коинов':
            self.res.configure(text = f'Недостаточно коинов')
            return
        if result[0] == 'Нет коинов':
            self.res.configure(text='Нет коинов')
            self.destroy()

        sign = result[3]
        self.res.configure(text = f'{result[0]}')
        self.balance.configure(text = f'Баланс: {self.list_int([result[1]])}')
        if sign == 'бумага':
            self.user_sign.configure(image=self.paper_img)
        if sign == 'ножницы':
            self.user_sign.configure(image=self.scissors_img)
        else:
            self.user_sign.configure(image=self.stone_img)
        self.choose_enemy_sign(result[2])
    
        
        
    def destroy(self):
        self.window.destroy()


    def run(self):
        self.stone_b.place(x=108, y=324)
        
        self.paper_b.place(x= 469, y= 324)
        
        self.scissors_b.place(x= 293, y= 324)
        
        self.res.place(x=340, y=260)
        
        self.balance.place(x=500, y=20)
        
        self.user_sign.place(x=165, y=150)
        
        self.enemy_sign.place(x=432, y=150)
        
        self.bet_entry.place(x=320, y=180)
        
        self.window.mainloop()
        
if __name__ == "__main__":
    main = WindowGame()
    main.run()