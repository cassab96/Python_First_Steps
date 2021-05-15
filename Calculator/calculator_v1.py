# Python Calculador 
# By cassabr

# Math library
import math

print("\n******************* Python Calculator *******************")

# Choose operation 
print("Select the number of the operation: \ n1 - Sum \ n2 - Subtraction \ n3 - Multiplication \ n4 - Division ")

operacao = int(input("Input the operation (1|2|3|4): "))

num1 = int(input("Input the first number: "))

num2 = int(input("Input the second number: "))


if operacao == 1:
	sum = num1 + num2
	print("%d + %d = %d" %(num1, num2, sum))
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
	print("Input value for operation is incorrect. Please try again from 1 to 4.")



