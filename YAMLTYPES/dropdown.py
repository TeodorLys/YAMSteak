from tkinter import LEFT
from customtkinter import CTkComboBox, CTk, StringVar
from YAMLTYPES.type_container import objs

class dropdown:
    def __init__(self, window: CTk, options: list):
        if len(options) == 0:
            print("No options added")
            return
        self.window = window
        self.options = options
        self.combo_var = StringVar(value=self.options[0])
        self.obj = None
        objs.append(self)
        
    def begin(self):
        self.obj = CTkComboBox(self.window, 
                               values=self.options, 
                               command=self.__command, 
                               variable=self.combo_var)
        self.obj.pack(padx=1,pady=10, anchor="w")

    def __command(self, option):
        print(f"Option {self.combo_var.get()}")