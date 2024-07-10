from YAMLTYPES import dropdown, subsection, tabs,entrybox, checkbox

class create_gui:
    def __init__(self):
        self.entry = []
        self.checkbox = []
        self.dropdown = []
        self.subsection = []
        self.custom_begin = False
        self.tab = None
    
    def handle_dict_objects(self, tab, data, custom_begin: bool = False):
        self.custom_begin = custom_begin
        if custom_begin:
            frame = tab
        else:
            self.tab = tabs.tabs(tab)
            frame = self.tab.add("default", True)
        for i in data.items():
            print(i)
            if not isinstance(i[1], dict):
                continue
            if "type" not in i[1]:
                continue
            if i[1]["type"] == "entry":
                self.__handle_entry_objects(frame, i[0], i[1])
            if i[1]["type"] == "checkbox":
                self.__handle_check_box(frame, i[0], i[1])
            if i[1]["type"] == "dropdown":
                self.__handle_dropdown(frame, i[0], i[1]["options"])
            if i[1]["type"] == "subsection":
                self.__handle_subsection(tab, i[0], i[1]["block"])

    def begin(self):
        for e in self.entry:
            e.begin()
        for c in self.checkbox:
            c.begin()
        for d in self.dropdown:
            d.begin()
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
        for s in self.subsection:
            final.update(s.get())
            
        return final

    def __handle_entry_objects(self, tab, name, data):
        self.entry.append(entrybox.entrybox(tab, name, name, self.custom_begin))
    
    def __handle_check_box(self, tab, name, data):
        self.checkbox.append(checkbox.checkbox(tab, name, self.custom_begin))
        
    def __handle_dropdown(self, tab, name, data):
        self.dropdown.append(dropdown.dropdown(tab, data, name, self.custom_begin))
        
    def __handle_subsection(self, tab, name, data):
        frame = self.tab.add(name, True)
        sec = subsection.subsection(frame, name)
        sec.create(data)
        self.subsection.append(sec)