#Crie um programa que solicite ao usuário um valor booleano (digite "True" ou "False") e exiba esse valor convertido para o tipo booleano.

valor = bool(input("Digite true or false: "))
tipo = type(valor)
print(F"O {valor} é {tipo} ")