"""
YAML type-keyword: multi_dropdown
"""
from CTkToolTip import CTkToolTip
from customtkinter import CTkButton, CTkComboBox, CTk, CTkFrame, StringVar
from YAMLTYPES.type_container import objs

class multi_dropdown:
    """
    * options: the options that should be available in the dropdown
    * name: name/key of the element ex. YAML: "
    -                                            height: 
    -                                                type: entry
    -                                         "
    - name = height   
    * description: tooltip text, if unassigned, tooltip is disabled
    * disable_container: if the ´begin´ funtion should be called through the type_container
    """
    def __init__(self, window: CTk, options: list, name:str, description: str = "", disable_container: bool = False):
        if len(options) == 0:
            print("No options added")
            return
        self.window = window
        self.options = options
        self.name = name
        self.combo_var = []
        self.obj = []
        self.add_btn = None
        self.remove_btn = None
        self.desc = description
        self.tooltip = []
        if not disable_container:
            objs.append(self)
        
    def begin(self):
        """
        Creates the first dropdown/combobox and if a 
        description is added we create the tooltip object
        Also create the +/- buttons for adding/removing another dropdown
        """
        cb_var = StringVar(value=self.options[0])
        self.combo_var.append(cb_var)
        self.obj.append(CTkComboBox(self.window, 
                               values=self.options, 
                               variable=self.combo_var))
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
        """
        Returns the object as a dict with its corresponding name/key
        """
        final_list = []
        for c in self.combo_var:
            if c.get() != "":
                final_list.append(c.get())
        return {self.name:final_list}

    def __add_command(self):
        """
        Adds a dropdown element after the first dropdown created
        """
        cb_var = StringVar(value=self.options[0])
        self.combo_var.append(cb_var)
        self.obj.append(CTkComboBox(self.window, 
                               values=self.options, 
                               variable=cb_var))
        if self.desc != "":
            self.tooltip.append(CTkToolTip(self.obj[len(self.obj) - 1], delay=0.5, message=self.desc))
        self.obj[len(self.obj) - 1].pack(after=self.obj[len(self.obj)-2],anchor="w")

    def __remove_command(self):
        """
        Remove the last created dropdown
        """
        if len(self.obj) == 1:
            return
        self.obj[len(self.obj)-1].pack_forget()
        self.obj.pop()
        if self.desc != "":
            self.tooltip.pop()
        
