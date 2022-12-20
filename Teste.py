# App de gerenciamento de horarios de professores

# Import das bibliotecas
from tkinter import *
from tkinter import messagebox

class app():
    def __init__(self):
        janela = Tk()
        janela.title("Gerenciamento de horarios escolares")
        janela.geometry('900x600')
        
        # Cabecalho
        def header():  
            lbl = Label(janela, text="Gerenciamento de horarios escolares")
            lbl.grid(column=0, row=0)
            
            lb2 = Label(janela, text="Feito em python")
            lb2.grid(column=1, row=0)
        # Corpo do projeto
        def body():
            txt = Entry(janela,width=10)
            txt.grid(column=4, row=0)
            
            lb3 = Label(janela, text="Botao")
            lb3.grid(column=3, row=1)    
            
            def button1():
                lb3.configure(text="Alterações foram Salvas")  
            
            btn = Button(janela, text="Botão", bg="blue", fg="white", command = button1)
            btn.grid(column=2, row=0)
        
        body()
        header()
        janela.mainloop()
app()