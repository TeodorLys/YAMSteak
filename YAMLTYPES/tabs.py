"""
Creates a tab view
"""

from customtkinter import CTkScrollableFrame, CTkTabview, CTk, BooleanVar
from YAMLTYPES.type_container import objs

class tabs:
    """
    * disable_container: if the 'begin' funtion should be called through the type_container
    """
    def __init__(self, window: CTk, disable_container: bool = False):
        self.window = window
        self.var = BooleanVar(value=False)
        self.obj = CTkTabview(self.window, width=400, height=350, anchor="w")
        if not disable_container:
            objs.append(self)


    def add(self, text: str, with_scroll: bool):
        """
        adds a tab to the tabview and
        if * with_scroll is TRUE
        we create a scrollable frame and returns that instead of
        the tab view object
        """
        tab = self.obj.add(text)
        frame = CTkScrollableFrame(tab, width=400, height=350)
        
        if with_scroll:
            frame.pack(expand=True)
            return frame
        return tab
    
    def begin(self):
        """
        Just adds the tab view to the window
        """
        self.obj.pack()