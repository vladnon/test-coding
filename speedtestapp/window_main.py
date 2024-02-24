from customtkinter import *
from speedtest import Speedtest


class Window:
    def __init__(self) -> None:
        self.window = CTk()
        self.window.geometry('200x150')
        self.window.title('Проверь скорость интернета!')
        self.window._set_appearance_mode('dark')
        self.window.resizable(False, False)


        self.download_speed = CTkLabel(self.window, text='Недостаточно данных', anchor=CENTER)
        self.upload_speed = CTkLabel(self.window, text='Недостаточно данных', anchor=CENTER)
        self.test_speed = CTkButton(self.window, text='Проверь свою скорость', command=self.main,  anchor=CENTER)


    def main(self):
        test = Speedtest()
        test.get_closest_servers()
        download_result = test.download()
        upload_result = test.upload()
        ping_result = test.results.ping
        self.download_speed.configure(text=f"Ваша скорость установки {download_result / 1024 / 1024:.2f}")
        self.upload_speed.configure(text=f"Ваша скорость загрузки {upload_result / 1024 / 1024:.2f}")



    def run(self):
        self.download_speed.pack(ipady=5)
        self.upload_speed.pack(ipady=5)
        self.test_speed.pack(ipady=5)
        self.window.mainloop()


    

if __name__ == '__main__':
    window = Window()
    window.run()