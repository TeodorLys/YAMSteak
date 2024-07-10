from customtkinter import CTkCheckBox, CTk, BooleanVar
from YAMLTYPES.type_container import objs

class checkbox:
    def __init__(self, window: CTk, text: str):
        self.window = window
        self.text = text
        self.var = BooleanVar(value=False)
        self.obj = None
        objs.append(self)

    def begin(self):
        self.obj = CTkCheckBox(self.window, 
                               text=self.text, 
                               command=self.__command,
                               variable=self.var,
                               onvalue=True,
                               offvalue=False)
        self.obj.pack()
        

    def __command(self):
        print(f"Checkbox {self.text} is {self.var.get()}")