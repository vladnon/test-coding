from customtkinter import *
from PIL import Image


class Secret(CTkToplevel):
    def __init__(self) -> None:
        self._set_appearance_mode('dark')
        self.resizable(False, False)
        self.title("Секрет")
        self.geometry('1820x980')
        
        self.image = CTkImage(light_image = Image.open('./типо игра/img/huy.jpg'), size=(1820, 980))
        
        self.label = CTkLabel(self, text=None, image=self.image)   
        self.label.pack()
        self.secret_window.mainloop()     
        
        
if __name__ == "__main__":
    window = Secret()
    window.run()