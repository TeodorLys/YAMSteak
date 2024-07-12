"""
YAML type-keyword: dropdown
"""
from CTkToolTip import CTkToolTip
from customtkinter import CTkComboBox, CTk, StringVar
from YAMLTYPES.type_container import objs

class dropdown:
    """
    * options: the options that should be available in the dropdown
    * name: name/key of the element ex. YAML: "
    -                                            height: 
    -                                                type: entry
    -                                         "
    - name = height   
    * description: tooltip text, if unassigned, tooltip is disabled
    * disable_container: if the 'begin' funtion should be called through the type_container
    """
    def __init__(self, window: CTk, options: list, name:str, description: str = "", disable_container: bool = False):
        if len(options) == 0:
            print("No options added")
            return
        self.window = window
        self.options = options
        self.name = name
        self.combo_var = StringVar(value=self.options[0])
        self.obj = None
        self.desc = description
        self.tooltip = None
        if not disable_container:
            objs.append(self)
        
    def begin(self):
        """
        Creates the dropdown/combobox and if a 
        description is added we create the tooltip object
        """
        self.obj = CTkComboBox(self.window, 
                               values=self.options,
                               variable=self.combo_var)
        if self.desc != "":
            self.tooltip = CTkToolTip(self.obj, delay=0.5, message=self.desc)
        self.obj.pack(padx=1,pady=10, anchor="w")
   
    def get(self):
        """
        Returns the object as a dict with its corresponding name/key
        """
        return {self.name:self.combo_var.get()}
