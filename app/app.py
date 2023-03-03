import tkinter as tk

root = tk.Tk()
root.title("Escolher uma Opção")

tk.Label(root, text="Escolha uma opção:").pack()

opcao = tk.StringVar()

opcoes = ['Adicionar', 'Excluir', 'Editar']

for opcao_atual in opcoes:
    tk.Radiobutton(root, text=opcao_atual, variable=opcao, value=opcao_atual).pack(anchor=tk.W)

def confirmar():
    root.destroy()

tk.Button(root, text="Confirmar", command=confirmar).pack()

root.mainloop()


