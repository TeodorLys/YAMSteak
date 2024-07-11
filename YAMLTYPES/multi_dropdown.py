from customtkinter import CTkButton, CTkComboBox, CTk, StringVar
from YAMLTYPES.type_container import objs

class multi_dropdown:
    def __init__(self, window: CTk, options: list, name:str, disable_container: bool = False):
        if len(options) == 0:
            print("No options added")
            return
        self.window = window
        self.options = options
        self.name = name
        self.combo_var = []
        self.obj = []
        self.add_btn = None
        if not disable_container:
            objs.append(self)
        
    def begin(self):
        # TODO add a "pack after" function / reseach this
        cb_var = StringVar(value=self.options[0])
        self.combo_var.append(cb_var)
        self.obj.append(CTkComboBox(self.window, 
                               values=self.options, 
                               variable=self.combo_var))
        self.add_btn = CTkButton(self.window, text="+", width=20, height=20, command=self.__command)
        self.obj.pack(padx=1,pady=10, anchor="w")
        self.add_btn.pack(padx=1,pady=1, anchor="w")
        
   
    def get(self):
        return {self.name:self.combo_var.get()}

    def __command(self):
        cb_var = StringVar(value=self.options[0])
        self.combo_var.append(cb_var)
        self.obj.append(CTkComboBox(self.window, 
                               values=self.options, 
                               variable=self.combo_var))
        self.obj[len(self.obj) - 1].pacl