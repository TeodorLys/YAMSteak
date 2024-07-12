from CTkToolTip import CTkToolTip
from customtkinter import CTkEntry, CTk
from YAMLTYPES.type_container import objs

class entrybox:
    def __init__(self, window: CTk, placeholder_text: str, name:str, description: str = "", disable_container: bool = False):
        self.window = window
        self.placeholder = placeholder_text
        self.name = name
        self.obj = None
        self.desc = description
        self.tooltip = None
        if not disable_container:
            objs.append(self)

    def begin(self):
        self.obj = CTkEntry(self.window, 
                               placeholder_text=self.placeholder)
        if self.desc != "":
            self.tooltip = CTkToolTip(self.obj, delay=0.5, message=self.desc)
        self.obj.pack(padx=1,pady=10, anchor="w")
        
    def get(self):
        return {self.name:self.obj.get()}