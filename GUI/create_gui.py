from dataclasses import dataclass
from YAMLTYPES import dropdown, multi_dropdown, subsection, tabs,entrybox, checkbox

class gui_objects:
    def __init__(self):
        self.name = ""
        self.entry = []
        self.checkbox = []
        self.dropdown = []
        self.multidropdown = []
        self.subsection = []
    
    def begin(self):
        for e in self.entry:
            e.begin()
        for c in self.checkbox:
            c.begin()
        for d in self.dropdown:
            d.begin()
        for m in self.multidropdown:
            m.begin()
        for s in self.subsection:
            s.begin()

    def get_data_block(self) -> dict:
        final = {}
        for e in self.entry:
            final.update(e.get())
        for c in self.checkbox:
            final.update(c.get())
        for d in self.dropdown:
            final.update(d.get())
        for m in self.multidropdown:
            final.update(m.get())
        for s in self.subsection:
            final.update(s.get())
        return final
    
    def get_data_block_with_top_name(self) -> dict:
        d = self.get_data_block()
        return {self.name:d}


class create_gui:
    def __init__(self):
        self.custom_begin = False
        self.tab = None
    
    def handle_dict_objects(self, tab, data, custom_begin: bool = False):
        self.custom_begin = custom_begin
        gui_obj = gui_objects()
        if custom_begin:
            frame = tab
        else:
            self.tab = tabs.tabs(tab)
            frame = self.tab.add("default", True)
        for i in data.items():
            if not isinstance(i[1], dict):
                continue
            if "type" not in i[1]:
                continue
            if i[1]["type"] == "entry":
                gui_obj.entry.append(self.__handle_entry_objects(frame, i[0]))
            if i[1]["type"] == "checkbox":
                gui_obj.checkbox.append(self.__handle_check_box(frame, i[0]))
            if i[1]["type"] == "dropdown":
                gui_obj.dropdown.append(self.__handle_dropdown(frame, i[0], i[1]["options"]))
            if i[1]["type"] == "multi_dropdown":
                gui_obj.multidropdown.append(self.__handle_multi_dropdown(frame, i[0], i[1]["options"]))
            if i[1]["type"] == "subsection":
                gui_obj.subsection.append(self.__handle_subsection(tab, i[0], i[1]["block"]))
        return gui_obj

    def __handle_entry_objects(self, tab, name):
        return entrybox.entrybox(tab, name, name, self.custom_begin)
        
    def __handle_check_box(self, tab, name):
        return checkbox.checkbox(tab, name, self.custom_begin)
        
    def __handle_dropdown(self, tab, name, data):
        return dropdown.dropdown(tab, data, name, self.custom_begin)
    
    def __handle_multi_dropdown(self, tab, name, data):
        return multi_dropdown.multi_dropdown(tab, data, name, self.custom_begin)
        
    def __handle_subsection(self, tab, name, data):
        frame = self.tab.add(name, True)
        sec = subsection.subsection(frame, name)
        sec.create(data)
        return sec