# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

import math

print("\n******************* Python Calculator *******************")

#Escolha da operação
print("Selecione o número da operação desejada: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

operacao = int(input("Digite sua opção (1|2|3|4): "))

num1 = int(input("Digite o primeiro número: "))

num2 = int(input("Digite o segundo número: "))


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



