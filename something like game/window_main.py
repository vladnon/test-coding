from customtkinter import *
from window_game import WindowGame
from PIL import Image
from secret_window import *

class Main(CTk):
    def __init__(self) -> None:
        # настройка окна
        self.window = CTk()
        self.window.geometry('300x150')
        self.window.title("Главное меню")
        self.window._set_appearance_mode('dark')
        self.window.resizable(width=False, height=False) 
        
        # импортирование картинок
        self.start_img = CTkImage(Image.open('./something like game/img/start.png'))
        self.close_img = CTkImage(Image.open('./something like game/img/close_.jpg'), size=(20, 25))
        
        # инициилизация перменных для экземпляров классов
        self.windowsec = None
        self.windowgame = None
    
        
        # создание кнопок
        self.start = CTkButton(self.window, text="Начать",image=self.start_img,command=self.start_game, font=CTkFont(family='Benzin-bold', size=20), text_color='black', fg_color='white', hover=False, bg_color='transparent') 
        self.close = CTkButton(self.window, text="Закрыть", image=self.close_img,command=self.close, font=CTkFont(family='Benzin-Bold', size=20), text_color='black', fg_color='white', hover=False, bg_color='transparent') 
        self.secret = CTkButton(self.window, text=None, fg_color='grey', width=4, height=4, hover=False, command=self.secret_func)
    
            
    
    def start_game(self):
        self.windowgame = WindowGame()
        self.windowgame.run()
        
    
    # я создаю здесь, ну и типо я не могу к ним обратиться из-за того, что после они удаляются
    def secret_func(self):
        self.windowsec = Secret()
        self.windowsec.run()


        
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
    

    