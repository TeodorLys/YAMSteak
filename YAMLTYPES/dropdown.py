from customtkinter import CTkComboBox, CTk, StringVar
from YAMLTYPES.type_container import objs

class dropdown:
    def __init__(self, window: CTk, options: list):
        self.window = window
        self.options = options
        self.combo_var = StringVar(value="")
        self.obj = None
        objs.append(self)
        
    def begin(self):
        self.obj = CTkComboBox(self.window, 
                               values=self.options, 
                               command=self.__command, 
                               variable=self.combo_var)
        
        self.obj.pack()
        
        


    def __command(self, option):
        print(f"Option {self.combo_var.get()}")