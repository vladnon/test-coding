from customtkinter import *


class Settings:
    def __init__(self) -> None:
        self.window = CTkToplevel()
        self.window.geometry('300x300')
        self.window.title("Настройки")
        self.window.resizable(width=False, height=False)
        self.window._set_appearance_mode('dark')
        
    def run(self):
        self.window.mainloop()
        
    def destroy(self):
        self.window.destroy()
        
        
if __name__ == "__main__":
    settings = Settings()
    settings.run()