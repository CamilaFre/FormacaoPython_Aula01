#Crie um programa que solicite o peso e a altura de uma pessoa e calcule o seu IMC (Índice de Massa Corporal) utilizando a fórmula: IMC = peso / (altura²)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura"))

imc = peso/(altura**2)

print(f"Sua altura em m é {altura} e seu peso é {peso}. Com isso, seu imc é {imc}.")