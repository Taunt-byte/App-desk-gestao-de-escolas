# App de gerenciamento de horarios de professores

# Import das bibliotecas
from tkinter import *
from tkinter import messagebox

class app():
    def __init__(self):
        janela = Tk()
        janela.title("Gerenciammento de horarios escolares")
   
        lbl = Label(janela, text="Ola Mundo")
        lbl.grid(column=0, row=0)
        
        janela.mainloop()
app()