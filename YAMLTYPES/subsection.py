"""
YAML type-keyword: subsection

Creates a new tab in the subtabs and creates a button that you can
add the items.

This is for when you need a list of dicts. example:
buttons:
  type: subsection
  block:
    height:
    type: entry
    width:
    type: entry
    clickable:
    type: checkbox
    
TODO: Add a remove button to remove a entry
MAYBE: add the items as entries instead of labels so they can be changed
after creation
"""
from CTkToolTip import CTkToolTip
from customtkinter import CTkButton, CTkLabel, CTkScrollableFrame, CTk, CTkToplevel
from GUI.create_gui import gui_objects

class subsection:
    """
    * name: name/key of the element ex. YAML: "
    -                                            height: 
    -                                                type: entry
    -                                         "
    - name = height   
    * description: tooltip text, if unassigned, tooltip is disabled
    """
    def __init__(self, window: CTk, name: str, description: str = ""):
        self.window = window
        self.obj = None
        self.name = name
        self.button = None
        self.block = None
        self.label = None
        self.toplevel = None
        self.gui = None
        self.data = []
        self.gui_obj = None
        self.desc = description
        self.tooltip = None

    def create(self, block: dict):
        """
        Creates a scrollable frame, 'Add' button, 
        Label with name and saves the block items
        """
        self.block = block
        self.obj = CTkScrollableFrame(self.window,width=350, height=1,
                                      orientation="vertical",fg_color="#3d3d3d")
        self.obj._scrollbar.configure(height=300)
        self.obj.pack(padx=1,pady=1, anchor="w")
        self.label = CTkLabel(self.obj,text=self.name)
        self.button = CTkButton(self.obj, text="Add", command=self.__command)
        if self.desc != "":
            self.tooltip = CTkToolTip(self.button, delay=0.5, message=self.desc)
        self.label.pack()
        self.button.pack()
        return self.obj
    
    def __command(self):
        """
        Opens a new window with the defined element from the block
        gotten from the 'create' function
        """
        self.toplevel = CTkToplevel(self.window)
        self.gui = create_gui()
        self.gui_obj = self.gui.handle_dict_objects(self.toplevel, self.block, True)
        self.gui_obj.begin()
        self.button = CTkButton(self.toplevel, text="Create", command=self.__on_create)
        self.button.pack()
        self.toplevel.grab_set()
        
    def get(self):
        """
        Returns the object as a dict with its corresponding name/key
        """
        return {self.name:self.data}

    def __on_create(self):
        """
        When pressing create, add the items as a labels to
        the main scrollable frame.
        Then destroy the window
        """
        self.toplevel.grab_release()
        last_dict = self.gui_obj.get_data_block()
        self.data.append(last_dict)
        for i in last_dict.items():
            l = CTkLabel(self.obj, text=i[0] + " -- " + str(i[1]))
            l.pack()
        l = CTkLabel(self.obj, text="------------------------------------------")
        l.pack()
        self.toplevel.destroy()