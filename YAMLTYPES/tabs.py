from customtkinter import CTkTabview, CTk, BooleanVar
from YAMLTYPES.type_container import objs

class tabs:
    def __init__(self, window: CTk):
        self.window = window
        self.var = BooleanVar(value=False)
        self.obj = CTkTabview(self.window, width=400, height=350)
        objs.append(self)


    def add(self, text: str):
        return self.obj.add(text)
    
    def begin(self):
        
        self.obj.pack()