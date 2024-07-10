import yaml
from YAMLTYPES import dropdown, tabs,entrybox, checkbox
from customtkinter import CTk

class config:
    def __init__(self, window: CTk):
        with open("config.yml", 'r') as file:
            self.config = yaml.safe_load(file)
        self.tb = tabs.tabs(window)
        self.entry = []
        self.checkbox = []
        self.dropdown = []
        self.__handle_tabs()

    def __handle_tabs(self):
        for i in self.config.items():
            tab = self.tb.add(i[0])
            self.__handle_tab_objects(tab, i[1])
            

    def __handle_tab_objects(self, tab, data):
        for i in data.items():
            if not isinstance(i[1], dict):
                continue
            if "type" not in i[1]:
                continue
            if i[1]["type"] == "entry":
                self.__handle_entry_objects(tab, i[0], i[1])
            if i[1]["type"] == "checkbox":
                self.__handle_check_box(tab, i[0], i[1])
            if i[1]["type"] == "dropdown":
                self.__handle_dropdown(tab, i[0], i[1]["options"])

    def __handle_entry_objects(self, tab, name, data):
        self.entry.append(entrybox.entrybox(tab, name))
    
    def __handle_check_box(self, tab, name, data):
        self.checkbox.append(checkbox.checkbox(tab, name))
        
    def __handle_dropdown(self, tab, name, data):
        self.dropdown.append(dropdown.dropdown(tab, data))