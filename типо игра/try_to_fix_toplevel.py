import customtkinter
from PIL import Image
from window_game import *

class ToplevelWindow(WindowGame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def run(self):
        super().run()


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.resizable(False, False)
        self.title("Main")

        self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow()
            self.toplevel_window.run()
        else:
            self.toplevel_window.focus()  # if window exists focus it


app = App()
app.mainloop()