from venv import create
import yaml
from YAMLTYPES import dropdown, subsection, tabs,entrybox, checkbox
from configuration.safe_assignment import safe_assignment
from configuration.create_gui import create_gui
from customtkinter import CTk

class config:
    def __init__(self, window: CTk):
        with open("config.yml", 'r') as file:
            self.config = yaml.safe_load(file)
        self.tb = tabs.tabs(window)
        self.assign = safe_assignment()
        self.gui = create_gui()
        self.__handle_tabs()
        

    def __handle_tabs(self):
        for i in self.config.items():
            tab = self.tb.add(i[0], False)
            self.gui.handle_dict_objects(tab, i[1])
            
        
