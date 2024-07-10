from YAMLTYPES import dropdown, checkbox, type_container, entrybox, tabs
from customtkinter import *
from configuration.config import config



window = CTk()
window.geometry("500x400")
cnf = config(window)
container = type_container.container()

container.handle()

window.mainloop()
