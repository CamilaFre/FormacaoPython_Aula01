#Crie um programa que solicite um número inteiro e exiba se ele é par ou ímpar (dica: use o operador %).
numero = int(input("Digite um número inteiro: "))
resto = numero%2
#print(resto)

if resto == 0 :
    print(f"O numero {numero} é par.")
else:
    print(f"O numero {numero} é ímpar.")