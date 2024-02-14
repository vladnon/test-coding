from customtkinter import *
from game import *
from PIL import Image
from  window_settings import *



from window_settings import *

class WindowGame:
    def __init__(self) -> None:
        # настройка окна
        self.window = CTk()
        self.window.geometry('700x500')
        self.window.title("Игра")
        self.window._set_appearance_mode('dark')
        self.window.resizable(width=False, height=False)
        self.user = Game()
        
        
        # создание изображение
        self.paper_img = CTkImage(light_image = Image.open('./типо игра/img/paper.png'), size=(120, 123))
        self.stone_img = CTkImage(light_image = Image.open('./типо игра/img/stone.png'), size=(156, 234))
        self.scissors_img = CTkImage(light_image = Image.open('./типо игра/img//scissors.png'), size=(126, 188))
        
        # создание кнопок
        # self.paper_b = CTkButton(self.window, image=self.paper_img,  command=self.paper, text=None, fg_color="transparent", hover=False, bg_color="transparent")
        # self.stone_b = CTkButton(self.window, text=None,  command=self.stone, fg_color='transparent', image=self.stone_img, hover=False)
        # self.scissors_b = CTkButton(self.window, text=None,  command=self.scissors, image=self.scissors_img, fg_color='transparent', hover=False)
        self.paper_b = CTkButton(self.window, text='Бумага', font=CTkFont(family='Benzin-Bold', size=20),  command=self.paper, fg_color="transparent", hover=False, bg_color="transparent", text_color='black')
        self.stone_b = CTkButton(self.window, font=CTkFont(family='Benzin-Bold', size=20), text='Камень',command=self.stone, fg_color='transparent', hover=False, text_color='black')
        self.scissors_b = CTkButton(self.window, text= 'Ножницы',font=CTkFont(family='Benzin-Bold', size=20),  command=self.scissors, fg_color='transparent', hover=False, text_color='black')
        
        
        # создание заголовков и прочего
        # self.balance = self.settings.balance.configure(text=self.settings.choose_level)
        self.balance = CTkLabel(self.window, text=10)
        # self.user_sign = CTkLabel(self.window ,image=self.paper_img, text=None)
        # self.enemy_sign= CTkLabel(self.window ,image=self.paper_img, text=None)
        self.user_sign =  CTkLabel(self.window, text='Нет', font=CTkFont(family='Benzin-Bold', size=20))
        self.enemy_sign= CTkLabel(self.window, text='Нет', font=CTkFont(family='Benzin-Bold', size=20))
        self.res = CTkLabel(self.window, text= 'Нет',  font=CTkFont(family='Benzin-Bold', size=15))
        self.bet = 5


    def window_exist(self):
        return self.window._window_exists()
        
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
        self.main(self.user.main('бумага', self.bet))
        
            
    def stone(self):
        self.main(self.user.main('камень', self.bet))
        

    def scissors(self):
        self.main(self.user.main('ножницы', self.bet))
        
    def main(self, result):
        if result[0] == 'Нет коинов':
            self.res.configure(text = 'Нет коинов')
            return 
        sign = f"{result[3]}"
        self.res.configure(text = f'{result[0]}')
        self.balance.configure(text = f'{self.list_int([result[1]])}')
        self.user_sign.configure(text=f'{result[3]}', font=CTkFont(family='Benzin-Bold', size=15))
        self.enemy_sign.configure(text=f'{result[2]}', font=CTkFont(family='Benzin-Bold', size=15))

    # def main(self, result):
    #     if result[0] == 'Ты проиграл все коины':
    #         self.res.configure(text = f'Результат игры: {result[0]}')
    #         return 
    #     sign = result[3]
    #     self.res.configure(text = f'Результат игры: {result[0]}')
    #     self.balance.configure(text = f'Баланс: {self.list_int([result[1]])}')
    #     if sign == 'бумага':
    #         self.user_sign.configure(image=self.paper_img)
    #     if sign == 'ножницы':
    #         self.user_sign.configure(image=self.scissors_img)
    #     else:
    #         self.user_sign.configure(image=self.stone_img)
    #     self.choose_enemy_sign(result[2])
    
        
        
    def destroy(self):
        self.window.destroy()


    def run(self):
        self.stone_b.place(x=108, y=324)
        
        self.paper_b.place(x= 469, y= 324)
        
        self.scissors_b.place(x= 293, y= 324)
        
        self.res.place(x=301, y=95)
        
        self.balance.place(x=450, y=261)
        
        self.user_sign.place(x=160, y=95)
        
        self.enemy_sign.place(x=428, y=95)
        self.window.mainloop()
        
if __name__ == "__main__":
    main = WindowGame()
    main.run()