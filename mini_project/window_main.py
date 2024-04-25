from customtkinter import *
from window_tasks import * 

class Window:
    def __init__(self) -> None:
        self.window = CTk()
        self.window._set_appearance_mode("dark")
        self.window.resizable(False, False)
        self.window.geometry('400x400')
        self.window.title("Главное меню")
        
        self.create_task = CTkButton(self.window, text='Создать новую задачу', command=self.create)
        
        
    def create(self):
        task = Task("Тест")
        task.run()
        
        
    def run(self):
        self.create_task.pack()
        
        
        self.window.mainloop()
        

if __name__ == "__main__":
    window = Window()
    window.run()