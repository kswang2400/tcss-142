# Lab Assignment 1, TCSS 142 Autumn 2014
# Due: Wednesday, Oct. 1, 2014, at the end of lab

# 1. Lecture Exercises



# 2. Python as Calculator / Operator Precedence

# a. Compute the number of seconds in 8 weeks

print("")
seconds = 8 * 7 * 24 * 60 * 60
print("8 weeks = " + str(seconds) + " seconds")
print("")

# b. Average age of five children, float

total = 5 + 7 + 11 + 12 + 14
averageAgeF = total / 5.0
print("The average age is " + str(averageAgeF))
print("")

# c. Average age, int. 

averageAgeI = int(averageAgeF)							# rounded down
print("The average age is " + str(averageAgeI))
print("")

# d. Modulo Operator

remainder1 = 3 % 2
print("3 % 2 = " + str(remainder1))
print("")

# e. Volume of sphere

def findVolume(radius):
	volume = 4 * 3.14 * (radius ** 3) / 3
	print("The volume of a sphere with radius of " + str(radius) + " is " + str(volume))
	return volume

findVolume(11)
findVolume(6.5)

# f. Four Expressions

print("")
print("7 / 3 * 1.2 + 3 / 2 = 4.3000001") 
print("7 // 3 * 1.2 + 3 / 2 = 3.9")
print("7 // 3 + 1.2 + 3 // 2 = 3.4")
print("7 / 3 * 1.2 + 3 // 2 = 3.80003")
print("")

# g. Parentheses

 # 30 - 3 ** 2 + 8 / 3 ** 2 * 10

 # (30 - (3 ** 2) + (8 / (3 ** 2) * 10))

print("")
print("30 - 3 ** 2 + 8 / 3 ** 2 * 10 = 29.8888")



 # 3. Basic Variables

# b. bday.py

def bday():
	myMonth = input("What is my birthday month? ")
	myDay = input("What is my birthday day? ")
	pMonth = input("What is my partner's birthday month? ")
	pDay = input("What is my partner's birthday day? ")
	pName = input("What is my partner's name? ")

	myBirthday = myMonth + "/" + myDay 
	pBirthday = pMonth + "/" + pDay

	output = "My birthday is " + myBirthday + " and " + pName + "'s birthday is " + pBirthday
	print(output)

bday()



