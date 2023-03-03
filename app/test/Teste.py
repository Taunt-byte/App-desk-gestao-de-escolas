# App de gerenciamento de horarios de professores

# Import das bibliotecas
import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Gerenciador de Horários")

# Cria um rótulo para exibir a data atual
data_atual = tk.Label(janela, text="Hoje é: " + str(datetime.date.today()))
data_atual.pack()

# Cria um rótulo e uma caixa de entrada para adicionar um novo evento
novo_evento_label = tk.Label(janela, text="Adicionar novo evento:")
novo_evento_label.pack()
novo_evento_entry = tk.Entry(janela)
novo_evento_entry.pack()

# Cria um botão para adicionar o novo evento
def adicionar_evento():
  evento = novo_evento_entry.get()
  # Adiciona o evento à lista de eventos
  eventos.append(evento)
  # Atualiza a lista de eventos na tela
  atualizar_lista_eventos()

adicionar_evento_botao = tk.Button(janela, text="Adicionar", command=adicionar_evento)
adicionar_evento_botao.pack()

# Cria uma lista para armazenar os eventos
eventos = []

# Cria uma área de texto para exibir a lista de eventos
lista_eventos = tk.Text(janela)

def atualizar_lista_eventos():
  # Limpa a área de texto
  lista_eventos.delete("1.0", "end")
  # Adiciona cada evento à lista
  for evento in eventos:
    lista_eventos.insert("end", evento + "\n")

# Exibe a lista de eventos pela primeira vez
atualizar_lista_eventos()
lista_eventos.pack()

# Executa o loop principal da GUI
janela.mainloop()
