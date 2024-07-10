from customtkinter import CTkEntry, CTk, BooleanVar
from YAMLTYPES.type_container import objs

class entrybox:
    def __init__(self, window: CTk, placeholder_text: str):
        self.window = window
        self.placeholder = placeholder_text
        self.var = BooleanVar(value=False)
        self.obj = None
        objs.append(self)

    def begin(self):
        self.obj = CTkEntry(self.window, 
                               placeholder_text=self.placeholder)
        self.obj.pack()