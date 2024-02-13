from customtkinter import *


class Settings:
    def __init__(self) -> None:
        self.window = CTk()
        self.window.geometry('350x300')
        self.window.title("Настройки")
        self.window.resizable(width=False, height=False)
        self.window._set_appearance_mode('dark')
        self.level_game_mod = CTkLabel(self.window, text='Выбери уровень сложности игры\nОни различаются лишь количество коинов в начале', anchor=CENTER, text_color='black', fg_color='transparent')
        self.choose_level_b = CTkComboBox(self.window, values=['Легкий(50 коинов)', 'Средний(20 коинов)', 'Тяжелый(5 коинов)'], fg_color='white', bg_color='black')

    def destroy(self):
        self.window.destroy()


    def choose_level(self):
        result = self.choose_level_b.cget()
        print(result)
        return result

    def run(self):
        self.level_game_mod.pack()
        self.choose_level_b.pack()
        self.window.mainloop()
        
    
        
        
        
if __name__ == "__main__":
    settings = Settings()
    settings.run()
    settings.choose_level()