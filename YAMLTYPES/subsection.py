from customtkinter import CTkButton, CTkLabel, CTkScrollableFrame, CTk, CTkToplevel
from GUI.create_gui import create_gui, gui_objects

class subsection:
    def __init__(self, window: CTk, name: str):
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

    def create(self, block: dict):
        self.block = block
        self.obj = CTkScrollableFrame(self.window,width=350, height=1,
                                      orientation="vertical",fg_color="#3d3d3d")
        self.obj._scrollbar.configure(height=300)
        self.obj.pack(padx=1,pady=1, anchor="w")
        self.label = CTkLabel(self.obj,text=self.name)
        self.button = CTkButton(self.obj, text="Add", command=self.__command)
        self.label.pack()
        self.button.pack()
        return self.obj
    
    def __command(self):
        self.toplevel = CTkToplevel(self.window)
        self.gui = create_gui()
        self.gui_obj = self.gui.handle_dict_objects(self.toplevel, self.block, True)
        self.gui_obj.begin()
        self.button = CTkButton(self.toplevel, text="Create", command=self.__on_create)
        self.button.pack()
        self.toplevel.grab_set()
        
    def get(self):
        return {self.name:self.data}

    def __on_create(self):
        self.toplevel.grab_release()
        last_dict = self.gui_obj.get_data_block()
        self.data.append(last_dict)
        for i in last_dict.items():
            l = CTkLabel(self.obj, text=i[0] + " -- " + str(i[1]))
            l.pack()
        l = CTkLabel(self.obj, text="------------------------------------------")
        l.pack()
        self.toplevel.destroy()