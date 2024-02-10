from customtkinter import *
from game import *
from PIL import Image



class WindowGame:
    def __init__(self) -> None:
        # настройка окна
        self.window = CTk()
        self.window.geometry('700x500')
        self.window.title("Игра")
        self.window._set_appearance_mode('dark')
        self.window.resizable(width=False, height=False)
        
        # 
        self.cost = 5
        self.res = CTkLabel(self.window, text= 'Результат игры: Недостаточно данных', font=CTkFont(family='FiraCode-medium', size=15), corner_radius=10, fg_color= 'white', text_color='black', height=40)
        self.user = Game()
        
        # создание изображение
        self.paper_img = CTkImage(light_image = Image.open('/home/vlad/Documents/test-python-main/типо игра/img/dick.png'), size=(125, 91))
        self.stone_img = CTkImage(light_image = Image.open('/home/vlad/Documents/test-python-main/типо игра/img/stone.png'), size=(130, 91))
        self.scissors_img = CTkImage(light_image = Image.open('/home/vlad/Documents/test-python-main/типо игра/img//scissors.png'), size=(87, 91))
        
        # создание кнопок
        self.paper_b = CTkButton(self.window, image=self.paper_img,  command=self.paper, text=None, fg_color='white', hover=False)
        self.stone_b = CTkButton(self.window, text=None,  command=self.stone, fg_color='white', image=self.stone_img, hover=False)
        self.scissors_b = CTkButton(self.window, text=None,  command=self.scissors, image=self.scissors_img, fg_color='white', hover=False)
        
        # создание заголовков и какой херни
        self.balance = CTkLabel(self.window, text=f'Баланс: {self.user.coins}', font=CTkFont(family='FiraCode-medium', size=15), corner_radius=10, fg_color= 'white', text_color='black', bg_color='transparent', height=40, width=20)
        self.entry_cost = CTkEntry(self.window)
        self.user_sign = CTkLabel(self.window ,image=self.paper_img, text=None)
        self.enemy_sign= CTkLabel(self.window ,image=self.paper_img, text=None)
        
    def list_int(self, nums) -> int:
        result = 0
        for num in nums:
            result += num
        return result
    
    def choose_enemy_sign(self, enemy):
        if enemy == 'бумага':
            self.enemy_sign.configure(image=self.paper_img)
        if enemy == 'камень':
            self.enemy_sign.configure(image=self.stone_img)
        if enemy == "ножницы":
            self.enemy_sign.configure(image=self.scissors_img)
       

    def paper(self):
        result = self.user.main('бумага', self.cost)
        self.res.configure(text = f'Результат игры: {result[0]}')
        self.balance.configure(text = f'Баланс: {self.list_int([result[1]])}')
        self.user_sign.configure(image=self.paper_img)
        self.choose_enemy_sign(result[2])
        
            
    def stone(self):
        result = self.user.main('камень', self.cost)
        self.res.configure(text = f'Результат игры: {result[0]}')
        self.balance.configure(text = f'Баланс: {self.list_int([result[1]])}')
        self.user_sign.configure(image=self.stone_img)
        self.choose_enemy_sign(result[2])
        
        
    def scissors(self):
        result = self.user.main('ножницы', self.cost)
        self.res.configure(text = f'Результат игры: {result[0]}')
        self.balance.configure(text = f'Баланс: {self.list_int([result[1]])}')
        self.user_sign.configure(image=self.scissors_img)
        self.choose_enemy_sign(result[2])

        
        
    def destroy(self):
        self.window.destroy()


    def run(self):
        self.stone_b.place(x=108, y=324)
        
        self.paper_b.place(x= 469, y= 324)
        
        self.scissors_b.place(x= 293, y= 324)
        
        self.res.place(x=148, y=261)
        
        self.balance.place(x=450, y=261)
        
        self.user_sign.place(x=151, y=95)
        
        self.enemy_sign.place(x=428, y=95)
        self.window.mainloop()
        
if __name__ == "__main__":
    main = WindowGame()
    main.run()