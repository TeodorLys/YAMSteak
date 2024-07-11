import yaml
from YAMLTYPES import subsection, tabs
from GUI.create_gui import create_gui, gui_objects
from customtkinter import CTk

class config:
    def __init__(self, window: CTk):
        with open("config.yml", 'r') as file:
            self.config = yaml.safe_load(file)
        self.tb = tabs.tabs(window)
        self.gui = create_gui()
        self.gui_obj = []
        self.__generate_gui()
        
    def generate_yaml(self):
        final = {}
        for g in self.gui_obj:
            final.update(g.get_data_block_with_top_name())
            
        with open('data.yml', 'w') as outfile:
            yaml.dump(final, outfile, default_flow_style=False)

    def __generate_gui(self):
        for i in self.config.items():
            tab = self.tb.add(i[0], False)
            _tmp_gui = self.gui.handle_dict_objects(tab, i[1])
            _tmp_gui.name = i[0]
            self.gui_obj.append(_tmp_gui)
            
