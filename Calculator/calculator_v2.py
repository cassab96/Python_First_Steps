# Calculador in Python
# By cassabr

# Development of the four basics operations using Python language. 
# Application of fundamental knowlegde - first challenge.


#import package
import time
import math

print("\n----------> Python Calculator <----------\n")

# Description
print("Select the operation: \n\n           Sum = + \n   Subtraction = - \nMultiplication = * ou x \n      Division = / \n\n")

def main():

	# Choose a math operation
	num1 = int(input("Number 1:      "))

	# Input first number
	operation = str(input("Operation:     "))

	# Input second number
	num2 = int(input("Number 2:      "))

	# Program:
	if operation == "+":
		su = num1 + num2
		print("             ______ \n\nResultado=     %d" %su)

	elif operation == "-":
		sub = num1 - num2
		print("             ______ \n\nResultado=     %d" %sub)

	elif operation == "*":
		mult = num1 * num2
		print("             ______ \n\nResultado=     %d" %mult)

	elif operation == "x":
		mult2 = num1 * num2
		print("             ______ \n\nResultado=     %d" %mult2)

	elif operation == "/":
		div = num1 / num2
		print("             ______ \n\nResultado=     %d" %div)
		
	else:
		print("Input value for operation is incorrect. Please try again.")
	
	
	time.sleep(3)
if __name__ == "__main__":
	main()
