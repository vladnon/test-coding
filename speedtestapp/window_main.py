from customtkinter import *
from main import *


class Window:
    def __init__(self) -> None:
        self.window = CTk()
        self.window.geometry('300x200')
        self.window.title('Проверь скорость интернета!')
        self.window._set_appearance_mode('light')
        self.window.resizable(False, False)


        self.download_speed = CTkLabel(self.window, text='Недостаточно данных', anchor=CENTER)
        self.upload_speed = CTkLabel(self.window, text='Недостаточно данных', anchor=CENTER)
        self.test_speed = CTkButton(self.window, text='Проверь свою скорость', command=self.main,  anchor=CENTER)


    def main(self):
        result = main()
        self.download_speed.configure(text=f"Ваша скорость установки {result[0] / 1024 / 1024:.2f}")
        self.upload_speed.configure(text=f"Ваша скорость загрузки {result[1] / 1024 / 1024:.2f}")



    def run(self):
        self.download_speed.place(x=80, y=20)
        self.upload_speed.place(x=80, y=60)
        self.test_speed.place(x=65, y=90)
        self.window.mainloop()


    

if __name__ == '__main__':
    window = Window()
    window.run()