from customtkinter import *
from game import *
from PIL import Image
import tkinter


class WindowGame:
    def __init__(self) -> None:
        # настройка окна
        self.window = CTkToplevel()
        self.window.geometry('650x400')
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
        self.stone_b = CTkButton(self.window, text=None,  command=self.stone, fg_color='transparent', image=self.stone_img, hover=False, bg_color="transparent")
        self.scissors_b = CTkButton(self.window, text=None,  command=self.scissors, image=self.scissors_img, fg_color='transparent', hover=False, bg_color="transparent")

        # создание заголовков и прочего
        self.balance = CTkLabel(self.window, font=CTkFont(family='Benzin-Bold', size=15), text=f'Баланс: {self.user.coins}')
        self.user_sign = CTkLabel(self.window ,image=self.paper_img, text=None)
        self.enemy_sign= CTkLabel(self.window ,image=self.paper_img, text=None)
        self.res = CTkLabel(self.window, text= 'Нет',  font=CTkFont(family='Benzin-Bold', size=15), anchor=CENTER, fg_color="transparent", bg_color="transparent")
        self.bet_entry = CTkEntry(self.window, placeholder_text='Ставка', font=CTkFont(family='Benzin-Bold', size=10), text_color='white', width=80, fg_color="transparent", bg_color="transparent")
        self.max = CTkLabel(self.window, text=10, font=CTkFont(family='Benzin-Bold', size=15), fg_color="transparent", bg_color="transparent")

    
            
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
        if self.bet_entry.get() == '':
            return
        bet = int(self.bet_entry.get())
        self.main(self.user.main('бумага', bet))
        
            
    def stone(self):
        if self.bet_entry.get() == '':
            return
        bet = int(self.bet_entry.get())
        self.main(self.user.main('камень', bet))
        

    def scissors(self):
        if self.bet_entry.get() == '':
            return
        bet = int(self.bet_entry.get())
        self.main(self.user.main('ножницы', bet))
        
    
    def focus(self):
        self.window.focus()
        
        
    def update_balance(self, result):
        self.balance.configure(text = f'Баланс: {self.list_int([result[1]])}')
        
        
    def update_res(self, result):
        self.res.configure(text = f'{result[0]}')
        
        
    def update_user(self, sign):
        if sign == 'бумага':
            self.user_sign.configure(image=self.paper_img)
        if sign == 'ножницы':
            self.user_sign.configure(image=self.scissors_img)
        else:
            self.user_sign.configure(image=self.stone_img)
            
            
    def update_max(self, result):
        if int(self.max._text) < result[1]:
            self.max.configure(text=result[1])
           
            
    def not_enough_coins(self, result):
        if result[0] == 'Недостаточно коинов':
            self.res.configure(text = f'Не хватает')
            return
        
        if result[0] == 'Нет коинов':
            self.destroy()

    def main(self, result):
        self.not_enough_coins(result)
        sign = result[3]
        self.update_user(sign)
        self.update_res(result)
        self.update_balance(result)
        self.update_max(result)
        self.choose_enemy_sign(result[2])
    
        
        
    def destroy(self):
        self.window.destroy()


    def run(self):
        self.stone_b.place(x=55, y=259)
        
        self.paper_b.place(x= 429, y= 259)
        
        self.scissors_b.place(x=240, y=259)
        
        self.res.place(x=282, y=125)
        
        self.balance.place(x=128, y=201)
        
        self.user_sign.place(x=77, y=93)
        
        self.enemy_sign.place(x=446, y=93)
        
        self.bet_entry.place(x=285, y=200)
        
        self.max.place(x=446, y=200)
        
        self.window.mainloop()
        
if __name__ == "__main__":
    main = WindowGame()
    main.run()