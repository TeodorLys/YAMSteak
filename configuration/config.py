"""
Handles the loading and deletegaing of the config file
Also generates the final output yaml file
"""

import yaml
from YAMLTYPES import tabs
from GUI.create_gui import create_gui
from customtkinter import CTk

class config:
    """
    Loads the yaml config file
    gives the data to the create_gui class
    generates the output
    """
    def __init__(self, window: CTk):
        with open("config.yml", 'r') as file:
            self.config = yaml.safe_load(file)
        self.tb = tabs.tabs(window)
        self.gui = create_gui()
        self.gui_obj = []
        self.__generate_gui()
        
    def generate_yaml(self):
        """
        Retrieves all gui_obj data with top name
        and adds it to a single dict object,
        then dumps it top a data.yml file
        TODO: another name of output
        """
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
            
