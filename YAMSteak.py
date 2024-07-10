from YAMLTYPES import dropdown, checkbox, type_container, entrybox
from customtkinter import *

window = CTk()
window.geometry("500x400")

container = type_container.container()

dp = dropdown.dropdown(window, ["1", "2", "help"])
ck = checkbox.checkbox(window, "test")
et = entrybox.entrybox(window, "HELP")


#dp.begin()
#ck.begin()

container.handle()

window.mainloop()
