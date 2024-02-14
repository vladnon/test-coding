from customtkinter import *
import  speedtest_cli 
import speedtest

class Window:
    def __init__(self) -> None:
        self.name = speedtest_cli.
        self.window = CTk()
        self.window.geometry('200x300')
        self.window.title('Проверь скорость интернета!')
        self.window._set_appearance_mode('light')
        self.window.resizable(False, False)


        self.download_speed_label = CTkLabel(self.window, text='Скорость установки ', anchor=CENTER)
        self.download_upload_label = CTkLabel(self.window, text='Скорость загрузки', anchor=CENTER)
        self.download_speed = CTkLabel(self.window, text='Недостаточно данных', anchor=CENTER)
        self.upload_speed = CTkLabel(self.window, text='Недостаточно данных', anchor=CENTER)
        self.test_speed = CTkButton(self.window, text='Проверь свою скорость', command=self.test,  anchor=CENTER)


    def test(self):
        pass



    def run(self):
        self.download_speed_label.place(x=40, y=40)
        self.download_upload_label.place(x=40, y=60)
        self.download_speed.place(x=40, y=100)
        self.upload_speed.place(x=40, y=120)
        self.test_speed.place(x=20, y=180)
        self.window.mainloop()


    

if __name__ == '__main__':
    window = Window()
    window.run()