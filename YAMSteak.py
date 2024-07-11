from YAMLTYPES import type_container
from customtkinter import CTk, CTkButton
from configuration.config import config



window = CTk()
window.geometry("500x500")
cnf = config(window)
container = type_container.container()

container.handle()

def command():
    cnf.generate_yaml()


generate_btn = CTkButton(window, text="Generate", command=command)
generate_btn.pack()


window.mainloop()

