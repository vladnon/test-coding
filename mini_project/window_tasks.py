from main import *
from customtkinter import *



class Task(BinaryHeap):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.window = CTkToplevel(fg_color="#00000000")
        self.window.title(self.name)
        self.window.geometry('400x400')
        
        
        self.label = CTkLabel(self.window, text=self.prt())
        
        
    def push_in_heap(self, key, node):
        self.append(key, node)
        
    
        
    def run(self):
        self.label.pack()
        self.window.mainloop()
    
    
    def prt(self):
        self.retur()
        
        
        
        
    
        
if __name__ == "__main__":
    window = Task("hg")
    window.run()