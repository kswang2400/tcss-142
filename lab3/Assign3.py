'''
Assignment 3, Lab 3
Kevin Wang
Oct 15, 2014
'''

# 2 Nested ifs and testing

gpa = float(input("Enter the gpa: "))

credits = 5

if gpa > 4.0 or gpa < 0.0:
    print("Well - this is not a valid GPA...")
    credits = 0
elif gpa >= 3.5 and gpa <= 4.0:
    print("I made the dean's list for this class!")
    if gpa == 4.0:
        print("I'm valedictorian for this class! Woo hoo!")


if gpa < 1.5:
    print("Uh-oh..I probably should have practiced a little more.")
    if gpa <= 0.7:
        credits = 0

print("Credits earned:", credits) 

# 3 for Loops

'''
sum of arithmetic series {1, 4, 7...}
'''
n = int(input("What is n for arithemtic series? "))
num = 1
sumNum = 1
list1 = [1]

for x in range(n-1):
	num += 3
	sumNum += num
	list1.append(num)

print(sumNum)
print(list1)

'''
sum of geometric series {1/2, 1/4, 1/8...}
'''

n1 = int(input("What is n for gemometric series? "))
num1 = 1/2
sumNum1 = 1/2
list2 = [1/2]

for x in range(n-1):
	num1 = num1 / 2
	sumNum1 += num1
	list2.append(num1) 

print(sumNum1)
print(list2)

'''
factorial of number n
'''

n = int(input("Factorial of n? "))
answer = 1

for x in range(1, n+1):
    answer *= x

print(answer)

# 4 Nested ifs and for

'''
print quadrant
'''

x = int(input("What is the x-coordinate? "))
y = int(input("What is the y-coordinate? "))

if x == 0 and y == 0:
	print("Origin")
elif x == 0:
	print("Lies on y-axis")
elif y == 0:
	print("lies on x-axis")
elif x > 0:
	if y > 0:
		print("Quadrant 1")
	else:
		print("Quadrant 4")
elif x < 0:
	if y > 0:
		print("Quadrant 2")
	else:
		print("Quadrant 3")

'''
calculate money
'''

days = int(input("How many days? "))

pennies = 1
sumPennies = 1
check = [1]

for time in range(days-1):
	pennies = pennies * 2
	check.append(pennies)
	sumPennies += pennies

print(check)
print(sumPennies)
print("Total = $" + str(round(sumPennies / 100, 2)))





