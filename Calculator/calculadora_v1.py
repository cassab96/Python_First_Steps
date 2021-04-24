# Calculador in Python
# Code created by cassab96

# Development of the four basics operations using Python language 
# Application of fundamental knowlegde - first challenge


import math

print("\n******************* Python Calculator *******************")

# Description
print("Selecione o número da operação desejada: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

# Choose a math operation
operacao = int(input("Digite sua opção (1|2|3|4): "))

# Input first number
num1 = int(input("Digite o primeiro número: "))

# Input second number
num2 = int(input("Digite o segundo número: "))

# Program:
if operacao == 1:
	soma = num1 + num2
	print("%d + %d = %d" %(num1, num2, soma))
elif operacao == 2:
	sub = num1 - num2
	print("%d - %d = %d" %(num1, num2, sub))
elif operacao == 3:
	mult = num1 * num2
	print("%d * %d = %d" %(num1, num2, mult))
elif operacao == 4:
	div = num1 / num2
	print("%d / %d = %d" %(num1, num2, div))
else:
	print("Valor de entrada para operação incorreto. Por favor, tente novamente de 1 a 4.")



