#TESTE 
# pergunta nome 
nome = input("Qual é o seu nome?")
# pergunta idade e tranforma para numero 
idade = int(input("Qual é a sua idade?"))
# verifica se a pessoa é maior de idade 
if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, voce é menor de idade.")
# pausa no final 
input ("Pressione Enter para sair...")