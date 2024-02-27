from customtkinter import *
from PIL import Image


class Secret:
    def __init__(self) -> None:
        self.secret_window = CTkToplevel()
        self.secret_window._set_appearance_mode('dark')
        self.secret_window.resizable(False, False)
        self.secret_window.title("Секрет")
        self.secret_window.geometry('1820x980')
        
        self.image = CTkImage(light_image = Image.open('./типо игра/img/huy.jpg'), size=(1820, 980))
        
        self.label = CTkLabel(self.secret_window, text=None, image=self.image)        
        
    def destroy(self):
        self.secret_window.destroy()
        
        
    def focus(self):
        self.secret_window.focus()
        
    def run(self):
        self.label.pack()
        self.secret_window.mainloop()
        
if __name__ == "__main__":
    window = Secret()
    window.run()