#Crie um programa que solicite dois números inteiros e mostre a divisão inteira e o resto da divisão do primeiro pelo segundo.

n1= int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
divint = n1//n2
resto = n1%n2

print(f"A divisão de {n1} por {n2} é {divint} e o resto é {resto}.")