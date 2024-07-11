from customtkinter import CTkComboBox, CTk, StringVar
from YAMLTYPES.type_container import objs

class dropdown:
    def __init__(self, window: CTk, options: list, name:str, disable_container: bool = False):
        if len(options) == 0:
            print("No options added")
            return
        self.window = window
        self.options = options
        self.name = name
        self.combo_var = StringVar(value=self.options[0])
        self.obj = None
        if not disable_container:
            objs.append(self)
        
    def begin(self):
        self.obj = CTkComboBox(self.window, 
                               values=self.options, 
                               command=self.__command, 
                               variable=self.combo_var)
        self.obj.pack(padx=1,pady=10, anchor="w")
   
    def get(self):
        return {self.name:self.combo_var.get()}

    def __command(self, option):
        print(f"Option {self.combo_var.get()}")