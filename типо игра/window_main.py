from customtkinter import *
from window_game import WindowGame
from PIL import Image
from secret_window import *

class Main(CTk):
    def __init__(self, *args, **kwargs) -> None:
        # настройка окна
        super().__init__(*args, **kwargs)
        self.geometry('300x150')
        self.title("Главное меню")
        self._set_appearance_mode('dark')
        self.resizable(width=False, height=False) 
        
        # импортирование картинок
        self.start_img = CTkImage(Image.open('./типо игра/img/start.png'))
        self.close_img = CTkImage(Image.open('./типо игра/img/close_.jpg'), size=(20, 25))
        
        # инициилизация перменных для экземпляров классов
        self.windowsec = None
        self.windowgame = None
    
        
        # создание кнопок
        self.start = CTkButton(self, text="Начать",image=self.start_img,command=self.start_game, font=CTkFont(family='Benzin-bold', size=20), text_color='black', fg_color='white', hover=False, bg_color='transparent') 
        self.close = CTkButton(self, text="Закрыть", image=self.close_img,command=self.close, font=CTkFont(family='Benzin-Bold', size=20), text_color='black', fg_color='white', hover=False, bg_color='transparent') 
        self.secret = CTkButton(self, text=None, fg_color='grey', width=4, height=4, hover=False, command=self.secret_func)
    
            
    
    def secret_func(self):
        if not self.windowsec or self.windowsec.winfo_exists():
            self.windowsec = WindowGame(self)
        else:
            self.windowsec.focus()
    
    # я создаю здесь, ну и типо я не могу к ним обратиться из-за того, что после они удаляются
    def start_game(self):
        if not self.windowgame or self.windowgame.winfo_exists():
            self.windowgame = WindowGame(self)
        else:
            self.windowgame.focus()

        
    def close(self):
        try:
            self.windowgame.destroy()
        except:
            pass
        try:
            self.windowsec.destroy()
        except:
            pass
        self.destroy()
        
    
    
    def run(self):
        self.start.pack(pady=25)
        self.close.pack()
        self.secret.pack(pady=15, padx=20)
        self.mainloop()
        
if __name__ == '__main__':
    start = Main()
    start.run()
    

    