from customtkinter import *
from window_game import WindowGame
from PIL import Image
from secret_window import *
from game import Game

class Main:
    def __init__(self) -> None:
        # настройка окна
        self.window = CTk()
        self.window.geometry('300x150')
        self.window.title("Главное меню")
        self.window._set_appearance_mode('dark')
        self.window.resizable(width=False, height=False) 
        
        # импортирование картинок
        self.start_img = CTkImage(Image.open('./типо игра/img/start.png'))
        self.close_img = CTkImage(Image.open('./типо игра/img/close_.jpg'), size=(20, 25))
        
        # инициилизация перменных для экземпляров классов
        self.windowsec = None
        self.windowgame = None
    
        
        # создание кнопок
        self.start = CTkButton(self.window, text="Начать",image=self.start_img,command=self.start_game, font=CTkFont(family='Benzin-bold', size=20), text_color='black', fg_color='white', hover=False, bg_color='transparent') 
        self.close = CTkButton(self.window, text="Закрыть", image=self.close_img,command=self.close, font=CTkFont(family='Benzin-Bold', size=20), text_color='black', fg_color='white', hover=False, bg_color='transparent') 
        self.secret = CTkButton(self.window, text=None, fg_color='grey', width=4, height=4, hover=False, command=self.secret_func)
    
            
    
    def secret_func(self):
        self.windowsec = Secret()
        self.windowsec.run()
    
    # я создаю здесь, ну и типо я не могу к ним обратиться из-за того, что после они удаляются
    def start_game(self):
        # self.windowgame = WindowGame()
        # self.windowgame.run()
        class WindowGame:
            def __init__(this):
                this.windowgame = CTkToplevel(self.window)
                this.windowgame.geometry('650x400')
                this.windowgame.title("Игра")
                this.windowgame._set_appearance_mode('dark')
                this.windowgame.resizable(width=False, height=False)
                this.user = Game()
                
                # создание изображение

                this.paper_img = CTkImage(light_image = Image.open('./типо игра/img/paper.png'), size=(125, 91))
                this.stone_img = CTkImage(light_image = Image.open('./типо игра/img/stone.png'), size=(130, 91))
                this.scissors_img = CTkImage(light_image = Image.open('./типо игра/img//scissors.png'), size=(87, 91))
                
                
                # создание кнопок
                this.paper_b = CTkButton(this.windowgame, image=this.paper_img,  command=this.paper, text=None, fg_color="transparent", hover=False, bg_color="transparent")
                this.stone_b = CTkButton(this.windowgame, text=None,  command=this.stone, fg_color='transparent', image=this.stone_img, hover=False, bg_color="transparent")
                this.scissors_b = CTkButton(this.windowgame, text=None,  command=this.scissors, image=this.scissors_img, fg_color='transparent', hover=False, bg_color="transparent")

                # создание заголовков и прочего
                this.balance = CTkLabel(this.windowgame, font=CTkFont(family='Benzin-Bold', size=15), text=f'Баланс: {this.user.coins}')
                this.user_sign = CTkLabel(this.windowgame ,image=this.paper_img, text=None)
                this.enemy_sign= CTkLabel(this.windowgame ,image=this.paper_img, text=None)
                this.res = CTkLabel(this.windowgame, text= 'Нет',  font=CTkFont(family='Benzin-Bold', size=15), anchor=CENTER, fg_color="transparent", bg_color="transparent")
                this.bet_entry = CTkEntry(this.windowgame, placeholder_text='Ставка', font=CTkFont(family='Benzin-Bold', size=10), text_color='white', width=80, fg_color="transparent", bg_color="transparent")
                this.max = CTkLabel(this.windowgame, text=10, font=CTkFont(family='Benzin-Bold', size=15), fg_color="transparent", bg_color="transparent")
            
            def list_int(this, nums) -> int:
                result = 0
                for num in nums:
                    result += num
                return result
            
        
            # выглядит, как костыль серьезно
            def choose_enemy_sign(this, enemy):
                if enemy == 'бумага':
                    this.enemy_sign.configure(image=this.paper_img)
                if enemy == 'камень':
                    this.enemy_sign.configure(image=this.stone_img)
                if enemy == "ножницы":
                    this.enemy_sign.configure(image=this.scissors_img)
            
            def paper(this):
                if this.bet_entry.get() == '':
                    return
                bet = int(this.bet_entry.get())
                this.main(this.user.main('бумага', bet))
                
                    
            def stone(this):
                if this.bet_entry.get() == '':
                    return
                bet = int(this.bet_entry.get())
                this.main(this.user.main('камень', bet))
                

            def scissors(this):
                if this.bet_entry.get() == '':
                    return
                bet = int(this.bet_entry.get())
                this.main(this.user.main('ножницы', bet))
                
            
            def focus(this):
                this.window.focus()

            def main(this, result):
                if result[0] == 'Недостаточно коинов':
                    this.res.configure(text = f'Не хватает')
                    return
                
                if result[0] == 'Нет коинов':
                    this.destroy()

                sign = result[3]
                this.res.configure(text = f'{result[0]}')
                this.balance.configure(text = f'Баланс: {this.list_int([result[1]])}')
                if int(this.max._text) < result[1]:
                    this.max.configure(text=result[1])
                if sign == 'бумага':
                    this.user_sign.configure(image=this.paper_img)
                if sign == 'ножницы':
                    this.user_sign.configure(image=this.scissors_img)
                else:
                    this.user_sign.configure(image=this.stone_img)
                this.choose_enemy_sign(result[2])
        
            
            
            def destroy(this):
                this.window.destroy()
                
            def run(this):
                this.stone_b.place(x=55, y=259)
                
                this.paper_b.place(x= 429, y= 259)
                
                this.scissors_b.place(x=240, y=259)
                
                this.res.place(x=282, y=125)
                
                this.balance.place(x=128, y=201)
                
                this.user_sign.place(x=77, y=93)
                
                this.enemy_sign.place(x=446, y=93)
                
                this.bet_entry.place(x=285, y=200)
                
                this.max.place(x=446, y=200)
                
                this.windowgame.mainloop()
        window_game = WindowGame()
        window_game.run()
        

        
    def close(self):
        try:
            self.windowgame.destroy()
        except:
            pass
        try:
            self.windowsec.destroy()
        except:
            pass
        self.window.destroy()
        
    
    
    def run(self):
        self.start.pack(pady=25)
        self.close.pack()
        self.secret.pack(pady=15, padx=20)
        self.window.mainloop()
        
if __name__ == '__main__':
    start = Main()
    start.run()
    

    