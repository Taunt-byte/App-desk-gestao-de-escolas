## É um aplicação que permite a montagem de horarios com dias,diciplinas e professores dessas diciplinas tudo feito em python.d
print("Bem vindo ao App criador de horarios para professores")

def hello():
	nome = input("Digite seu nome: ")
	print("seja bem vindo: ",nome,)

def diciplinas():
    dic = input("Digite a sua diciplina")
    resposta = input("Voce deseja escolher adicionar outra diciplina Sim(1) Não (2)")
    if (resposta == 2): 
        dic2 = input("Digite a sua diciplina")
    else:
       	print("")
hello()
diciplinas()
    