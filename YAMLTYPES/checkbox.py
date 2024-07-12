from CTkToolTip import CTkToolTip
from customtkinter import CTkCheckBox, CTk, BooleanVar
from YAMLTYPES.type_container import objs

class checkbox:
    def __init__(self, window: CTk, text: str, description: str = "", disable_container: bool = False):
        self.window = window
        self.text = text
        self.var = BooleanVar(value=False)
        self.obj = None
        self.desc = description
        self.tooltip = None
        if not disable_container:
            objs.append(self)

    def begin(self):
        self.obj = CTkCheckBox(self.window, 
                               text=self.text, 
                               command=self.__command,
                               variable=self.var,
                               onvalue=True,
                               offvalue=False)
        if self.desc != "":
            self.tooltip = CTkToolTip(self.obj, delay=0.5, message=self.desc)
        self.obj.pack(padx=1,pady=10, anchor="w")

    def get(self):
        return {self.text:self.var.get()}

    def __command(self):
        print(f"Checkbox {self.text} is {self.var.get()}")