'''
Assignment 4
Kevin Wang
10/22/14
'''

from random import randint

# a. do you want to hear again?

# Basic while loop exercises

# def run():
# 	print("She sells seashells by the seashore.")
# 	repeat = input("Do you want to hear it again? ")
# 	if repeat == 'y':
# 		run()

# run()

print("\n2a. Selling seashells\n")
do = True
while do is True:
	print("She sells seashells by the seashore.")
	repeat = input("Do you want to hear it again? ")
	if repeat != 'y':
		do = False

# b. number at least 900

print("\n2b. Print until number is at least 900\n")
input("Press enter to continue...")
num = randint(0, 1000)
counter = 1
print("Number {}: ".format(counter), num)

# print(num)
while num < 900:
	num = randint(0, 1000)
	counter += 1
	print("Number {}: ".format(counter), num)

print("Tries:", counter)

# c. sentinel loop max and min

print("\n2c. Sentinel loop and find max and min\n")
input("Press enter to continue...")

series = []
num1 = int(input("Enter a number (-1 to quit): "))
series.append(num1)

while num1 != -1:
	series.append(num1)
	num1 = int(input("Enter a number (-1 to quit): "))
	
print("Maximum was", max(series))
print("Minimum was", min(series))

# num = int(input("enter a number, -1 to quit: "))
# sentinel = 0
# maximum = 0
# minimum = 0
# first = True

# while sentinel != -1:
# 	if first == True:
# 		backup = num
# 		minimum = num
# 	if num > minimum:
# 		maximum = num
# 	if num < minimum:
# 		minimum = num
# 	num = int(input("enter a number, -1 to quit: "))
# 	first = False
# 	if num == -1:
# 		if maximum == 0:
# 			maximum = backup
# 		print("Max: ", maximum)
# 		print("Min: ", minimum)
# 		sentinel = -1

# 3. For loop trace

# 4. Problem solving with loops

print("\n4a. Find out how many payments to pay off balance\n")
input("Press enter to continue...")
def pay():	
	balance = int(input("Balance: "))
	month = int(input("Monthly payment: "))

	newBalance = balance
	payment = 0

	while newBalance != 0:
		newBalance = newBalance - month
		payment += 1
		if newBalance < 0:
			newBalance = 0
		print("Balance after payment {} is {}".format(payment, newBalance))

	again = input("Do you want to play again? Enter y for yes, n for no: ")
	if again == "y":
		pay()

pay()

# b. Guess a number between 1 and 20

print("\n4b. Guess a number between 1 and 20\n")
input("Press enter to continue...")
def play():
	target = randint(1, 20)
	guess = int(input("Guess a number: "))
	tries = 1
	while guess != target:
		tries += 1
		if guess > target:
			print("\ntoo high\n")
			guess = int(input("Try again: "))
		elif guess < target:
			print("\ntoo low\n")
			guess = int(input("Try again: "))

	if guess == target:
		print("You got it. The number was {}\nYou got it in {} tries.".format(target, tries))

	again = input("Do you want to play again? Enter y for yes, n for no: ")
	if again == "y":
		play()

play()


