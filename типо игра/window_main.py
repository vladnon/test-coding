from customtkinter import *
import window_game
from window_settings import Settings
from PIL import *

class Main:
    def __init__(self) -> None:
        self.window = CTk()
        self.window.geometry('300x200')
        self.window.title("Главное меню")
        self.count_win_game = 0
        self.count_win_settings = 0
        self.window._set_appearance_mode('dark')
        self.window.resizable(width=False, height=False)
        self.start = CTkButton(self.window, text="Начать", anchor=CENTER, command=self.start_game, font=CTkFont(family='FiraCode-Medium', size=20), text_color='black', fg_color='grey', hover_color='white') 
        self.settings = CTkButton(self.window, text="Настройки", anchor=CENTER, command=self.settings, font=CTkFont(family='FiraCode-Medium', size=20), text_color='black', fg_color='grey', hover_color='white')
        self.close = CTkButton(self.window, text="Закрыть", anchor=CENTER, command=self.close, font=CTkFont(family='FiraCode-Medium', size=20), text_color='black', fg_color='grey', hover_color='white') 
        
            

    def start_game(self):
        self.count_win_game += 1
        if self.count_win_game > 1:
            return
        self.windowgame = window_game.WindowGame()
        self.windowgame.run()
        
        
    def settings(self):
        self.count_win_settings += 1
        if self.count_win_settings > 1:
            return
        self.windowsettings = Settings()
        self.windowsettings.run()
        
        
    def close(self):
        try:
            self.windowgame.destroy()
            self.count_win_game -= 1
        except:
            pass
        try:
            self.windowsettings.destroy()
            self.count_win_settings -= 1
        except:
            pass
        self.window.destroy()
    
    
    def run(self):
        self.start.pack(pady=25)
        self.settings.pack(pady=5)
        self.close.pack(pady=25)
        self.window.mainloop()
        
if __name__ == '__main__':
    start = Main()
    start.run()
    