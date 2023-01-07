import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

# Cria um rótulo
label = tk.Label(janela, text="Olá, mundo!")
label.pack()

# Cria um botão
botao = tk.Button(janela, text="Clique aqui")
botao.pack()

# Executa o loop principal da GUI
janela.mainloop()
