from customtkinter import CTkEntry, CTk
from YAMLTYPES.type_container import objs

class entrybox:
    def __init__(self, window: CTk, placeholder_text: str, name:str, disable_container: bool = False):
        self.window = window
        self.placeholder = placeholder_text
        self.name = name
        self.obj = None
        if not disable_container:
            objs.append(self)

    def begin(self):
        self.obj = CTkEntry(self.window, 
                               placeholder_text=self.placeholder)
        self.obj.pack(padx=1,pady=10, anchor="w")
        
    def get(self):
        return {self.name:self.obj.get()}