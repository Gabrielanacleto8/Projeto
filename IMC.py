def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade grau 1"
    elif 35.0 <= imc <= 39.9: 
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"
    
    # Entrada de dados 
peso = float (input("Digite seu peso (kg):"))
altura = float(input("Digite sua altura (m):"))

# Calculo IMC
imc = peso / (altura ** 2)

# Classificacao 
classificacao = classificar_imc(imc)

#Saida 
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}" )
input ("Pressione Enter para sair...")