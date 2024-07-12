"""
YAML type-keyword: checkbox
"""
from CTkToolTip import CTkToolTip
from customtkinter import CTkCheckBox, CTk, BooleanVar
from YAMLTYPES.type_container import objs

class checkbox:
    """
    * text: what text should be after the checkbox
    * description: tooltip text, if unassigned, tooltip is disabled
    * disable_container: if the ´begin´ funtion should be called through the type_container
    """
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
        """
        Creates the checkbox and if a 
        description is added we create the tooltip object
        """

        self.obj = CTkCheckBox(self.window, 
                               text=self.text, 
                               variable=self.var,
                               onvalue=True,
                               offvalue=False)
        if self.desc != "":
            self.tooltip = CTkToolTip(self.obj, delay=0.5, message=self.desc)
        self.obj.pack(padx=1,pady=10, anchor="w")

    def get(self):
        """
        Returns the object as a dict with its corresponding name/key
        """
        return {self.text:self.var.get()}