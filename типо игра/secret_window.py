from customtkinter import *
from PIL import Image


class Secret(CTkToplevel):
    def __init__(self) -> None:
        self.secretwin = CTkToplevel()
        self.secretwin._set_appearance_mode('dark')
        self.secretwin.resizable(False, False)
        self.secretwin.title("Секрет")
        self.secretwin.geometry('1820x980')
        
        self.image = CTkImage(light_image = Image.open('./типо игра/img/ok.jpg'), size=(1820, 980))
        
        self.label = CTkLabel(self.secretwin, text=None, image=self.image)   
        
        
    def destroy(self):
        self.window.destroy()
        
    def run(self):
        self.label.pack()
        self.secretwin.mainloop()
        
        
if __name__ == "__main__":
    window = Secret()
    window.run()