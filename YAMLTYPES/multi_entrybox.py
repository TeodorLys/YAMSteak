from CTkToolTip import CTkToolTip
from customtkinter import CTkButton, CTkEntry, CTk, CTkFrame, StringVar
from YAMLTYPES.type_container import objs

class multi_entrybox:
    def __init__(self, window: CTk, placeholder_text: str, name:str, description: str = "", disable_container: bool = False):
        self.window = window
        self.placeholder = placeholder_text
        self.name = name
        self.obj = []
        self.add_btn = None
        self.remove_btn = None
        self.desc = description
        self.tooltip = []
        if not disable_container:
            objs.append(self)
        
    def begin(self):
        self.obj.append(CTkEntry(self.window, 
                               placeholder_text=self.placeholder))
        self.btn_frame = CTkFrame(self.window)
        self.add_btn = CTkButton(self.btn_frame, text="+", width=20, height=20, command=self.__add_command)
        self.remove_btn = CTkButton(self.btn_frame, text="-", width=20, height=20, command=self.__remove_command)
        if self.desc != "":
            self.tooltip.append(CTkToolTip(self.obj[len(self.obj) - 1], delay=0.5, message=self.desc))
        self.obj[len(self.obj) - 1].pack(padx=1,pady=1, anchor="w")
        self.btn_frame.pack(anchor="w")
        self.add_btn.grid(column=0, row=0)
        self.remove_btn.grid(column=1, row=0)

    def get(self):
        final_list = []
        for c in self.obj:
            if c.get() != "":
                final_list.append(c.get())
        return {self.name:final_list}

    def __add_command(self):
        cb_var = StringVar(value=self.options[0])
        self.obj.append(CTkEntry(self.window, 
                               placeholder_text=self.placeholder))
        if self.desc != "":
            self.tooltip.append(CTkToolTip(self.obj[len(self.obj) - 1], delay=0.5, message=self.desc))
        self.obj[len(self.obj) - 1].pack(after=self.obj[len(self.obj)-2],anchor="w")

    def __remove_command(self):
        if len(self.obj) == 1:
            return
        self.obj[len(self.obj)-1].pack_forget()
        self.obj.pop()
        if self.desc != "":
            self.tooltip.pop()