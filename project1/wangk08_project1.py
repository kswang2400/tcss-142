'''
Programming Assignment 1
TCSS142 Autumn 2014
Due: Friday, Nov. 14, 8am
Kevin Wang
'''

def main():
	# The program is repeated as many times as the user wishes
	repeat = True	
	while repeat:
		# Inputs two Roman Numerals and echoes the arabic notation
		num1 = input("\nEnter the first number: ").upper()
		num1arabic = romanToArabic(num1)
		print("\nThe first number is", num1arabic, "\n")

		num2 = input("Enter the second number ").upper()
		num2arabic = romanToArabic(num2)
		print("\nThe second number is", num2arabic, "\n")

		# Performs valid operations
		result = validOperation(num1arabic, num2arabic)

		# converts arabic result to Roman (rounded because no decimals in Roman)
		resultRoman = arabicToRoman(round(result))
		print("\nThe result is", resultRoman, "({})".format(result))

		# Asks the user if they would like to repeat
		repeat = input("\nDo you want to repeat this program? Y/N ").upper()
		if repeat == "N":
			print("\nGood job, you're done\n")
			repeat = False

def validOperation(num1, num2):
	# Checks to make sure arithmetic operation is valid
	validOperation = False
	while not validOperation:
		operation = input("Enter the desired arithmetic operation: ")
		if operation == "+":
			result = num1 + num2
			validOperation = True
		elif operation == "-":
			result = num1 - num2
			validOperation = True
		elif operation == "*":
			result = num1 * num2
			validOperation = True
		elif operation == "/" or operation == "%":
			if num2 == 0:
				print("\nSorry, cannot divide by zero.")
				# Asks for a new num2 
				num2 = input("\nEnter the second number ").upper()
				num2 = romanToArabic(num2)
				print("\nThe second number is", num2, "\n")
			elif operation == "/":
				result = num1 / num2
				validOperation = True
			else:
				result = num1 % num2
				validOperation = True
		else:
			print("\nPlease enter a valid operation\n")
	return result

def validRoman(Roman):
	# makes sure Roman Numeral is valid
	if Roman == '0':
		return True
	else:	
		for n in Roman.upper():
			if n not in "MDCLXVI":
				return False
			else:
				return True

def romanToArabic(Roman):	# convert Roman Numerals to arabic numbers
	# if Roman Numeral not valid, asks for input again
	while not validRoman(Roman):
		print("Not a valid Roman Numeral, please try again")
		Roman = input("Please enter a Roman Numeral ").upper()
		validRoman(Roman)

	number = 0
	# iterate through each letter and add value to number
	for n in Roman:
		if n == "M":
			number += 1000
		elif n == "D":
			number += 500
		elif n == "C":
			number += 100
		elif n == "L":
			number += 50
		elif n == "X":
			number += 10
		elif n == "V":
			number += 5
		elif n == "I":
			number += 1

	return number

def arabicToRoman(arabic):	# convert arabic numbers to Roman Numerals
	number = ""

	# if arabic not positive, return '0' or add negative sign in front
	if arabic == 0:
		number = "0"
	elif arabic < 0:
		number = "-"
		arabic *= -1

	# Subtract arabic number down to zero and replace with Roman symbols
	while arabic > 0:
		if arabic // 1000 > 0:
			number += "M" * (arabic // 1000)
			arabic = arabic % 1000
		if arabic // 500 > 0:
			number += "D" * (arabic // 500)
			arabic = arabic % 500
		if arabic // 100 > 0:
			number += "C" * (arabic // 100)
			arabic = arabic % 100
		if arabic // 50 > 0:
			number += "L" * (arabic // 50)
			arabic = arabic % 50
		if arabic // 10 > 0:
			number += "X" * (arabic // 10)
			arabic = arabic % 10
		if arabic // 5 > 0:
			number += "V" * (arabic // 5)
			arabic = arabic % 5
		if arabic // 1 > 0:
			number += "I" * (arabic // 1)
			arabic = arabic % 1

	return number

main()


