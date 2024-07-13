"""
Handles the creation of each GUI type (YAMLTYPES)
"""
from YAMLTYPES import dropdown, multi_dropdown, multi_entrybox, tabs,entrybox, checkbox
from CTkToolTip import CTkToolTip

class gui_objects:
    """
    Contains lists of all objects that is created
    """
    def __init__(self):
        self.name = ""
        self.entry = []
        self.multientry = []
        self.checkbox = []
        self.dropdown = []
        self.multidropdown = []
        self.listblock = []
    
    def begin(self):
        """
        Calls begin on all objects that exists in the lists
        """
        for e in self.entry:
            e.begin()
        for c in self.checkbox:
            c.begin()
        for d in self.dropdown:
            d.begin()
        for m in self.multidropdown:
            m.begin()
        for l in self.listblock:
            l.begin()

    def get_data_block(self) -> dict:
        """
        Compiles the data entered in the objects 
        into a single dict object
        """
        final = {}
        for e in self.entry:
            final.update(e.get())
        for c in self.checkbox:
            final.update(c.get())
        for d in self.dropdown:
            final.update(d.get())
        for m in self.multidropdown:
            final.update(m.get())
        for l in self.listblock:
            final.update(l.get())
        return final
    
    def get_data_block_with_top_name(self) -> dict:
        """
        Compiles the data entered in the objects 
        into a single dict object with the top name. example
        buttons:
          type: listblock
          block:
            height:
            type: entry
            width:
            type: entry
            clickable:
            type: checkbox

        top_name = buttons
        """
        d = self.get_data_block()
        return {self.name:d}


class create_gui:
    """
    Handles the types entered in the config.yml file.
    """
    def __init__(self):
        self.custom_begin = False
        self.tab = None
    
    def handle_dict_objects(self, tab, data, custom_begin: bool = False):
        """
        Delegates function calls from the config data
        * tab: the frame we will add the gui elements
        * data: the data to handle (dict)
        * custom_begin: if the elements should register them selfs in the
        - type_container or be 'begun' manually
        """
        self.custom_begin = custom_begin
        gui_obj = gui_objects()
        last_description = ""
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
            if "description" in i[1]:
                last_description = i[1]["description"]
            if i[1]["type"] == "entry":
                gui_obj.entry.append(self.__handle_entry_objects(frame, i[0], last_description))
            if i[1]["type"] == "multi_entry":
                gui_obj.multientry.append(self.__handle_multi_entry_objects(frame, i[0], last_description))
            if i[1]["type"] == "checkbox":
                gui_obj.checkbox.append(self.__handle_check_box(frame, i[0], last_description))
            if i[1]["type"] == "dropdown":
                gui_obj.dropdown.append(self.__handle_dropdown(frame, i[0], i[1]["options"], last_description))
            if i[1]["type"] == "multi_dropdown":
                gui_obj.multidropdown.append(self.__handle_multi_dropdown(frame, i[0], i[1]["options"], last_description))
            if i[1]["type"] == "listblock":
                gui_obj.listblock.append(self.__handle_listblock(tab, i[0], i[1]["block"], last_description))
        return gui_obj

    def __handle_entry_objects(self, tab, name, description):
        return entrybox.entrybox(tab, name, name, description, self.custom_begin)

    def __handle_multi_entry_objects(self, tab, name, description):
        return multi_entrybox.multi_entrybox(tab, name, name, description, self.custom_begin)
        
    def __handle_check_box(self, tab, name, description):
        return checkbox.checkbox(tab, name, description, self.custom_begin)
        
    def __handle_dropdown(self, tab, name, data, description):
        return dropdown.dropdown(tab, data, name, description, self.custom_begin)
    
    def __handle_multi_dropdown(self, tab, name, data, description):
        return multi_dropdown.multi_dropdown(tab, data, name, description, self.custom_begin)
        
    def __handle_listblock(self, tab, name, data, description):
        frame = self.tab.add(name, True)
        from YAMLTYPES import listblock
        sec = listblock.listblock(frame, name, description)
        sec.create(data)
        return sec