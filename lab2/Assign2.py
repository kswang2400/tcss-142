# Assignment 2

# 2. Formatting

print("")
s1 = "Mine"
s2 = "Yours"
i1 = 123
i2 = 5

print('{:>10}'.format(s1) + '{:>10}'.format(s2))
print('{:>10}'.format(str(i1)) + '{:>10}'.format(str(i2)))
print('{:>0}'.format(s1) + '{:>11}'.format(s2))
print('{:>0}'.format(str(i1)) + '{:>8}'.format(str(i2)))


print('{:<6}'.format("") + '{:<9}'.format(s1) + '{:<0}'.format(s2))
print('{:<6}'.format("") + '{:<9}'.format(str(i1)) + '{:<0}'.format(str(i2)))
print('{:<10}'.format(s1) + '{:<10}'.format(s2))
print('{:<10}'.format(str(i1)) + '{:<10}'.format(str(i2)))
print("")

d1 = 123.4
d2 = 3.1315926535

print('{:>10}'.format(d1) + '{:>10}'.format(d2))
# field too small, doesn't cut off (minimum field width)
print("")

print('{:<2}'.format(s1) + '{:<2}'.format(i1)) 	
# field too small, places i1 next to s1
print("")

# 3. Boolean Expressions

int1 = 12
int2 = 9
int3 = 8

print(
	int1 > int2 and int2 < int3,				# False, True and False
	int1 < int3 or int3 > int2,					# False, False or False
	int1 <= int2 - 6,							# False, 12 <= 3 is False
	int2 <= int1 + 5 or int3 >= int2 - 5,		# True, True or True
	not(int1 < 30),								# False, not True
	not(int2 == int1 and int3 == int1),			# True, not(False and False), not(False)
	not(int1 > 5) and not (int2 < 17), "\n"		# False, not(True) and not(True), False and False
)			

# b. Translate

temp1 = 54
temp2 = 55
temp3 = 68
temp4 = 69

def rangeT(temp):
	if temp >= 55 and temp <= 68:
		print(True)
	else:
		print(False)

rangeT(temp1)		# False
rangeT(temp2)		# True
rangeT(temp3)		# True
rangeT(temp4)		# False
print("")

#####

stud1 = (55, 2.5)	
stud2 = (15, 3.5)
stud3 = (25, 3.6)
stud4 = (23, 4)

def check(student):
	if student[0] >= 25 and student[1] >= 3.5:
		print(True)
	else:
		print(False)

check(stud1)		# False
check(stud2)		# False
check(stud3)		# True
check(stud4)		# False
print("")

#####

weather1 = (55, 91)
weather2 = (70, 70)
weather3 = (45, 45)
weather4 = (0, 0)

def verify(weather):
	if weather[0] <= 70 and weather[1] >= 70:
		print(True)
	else:
		print(False)

verify(weather1)	# True
verify(weather2)	# True
verify(weather3)	# False
verify(weather4)	# False
print("")

#####

p1 = (35, 40000)
p2 = (40, 40000)
p3 = (50, 60000)
p4 = (25, 50000)

def ageInc(person):
	if person[0] > 35 and person[1] >= 50000:
		print(True)
	else:
		print(False)

ageInc(p1)			# False
ageInc(p2)			# False
ageInc(p3)			# True
ageInc(p4)			# False
print("")

# 3. Truth Tables and Simple if

num = input("Enter a number from 1 to 7 ")

days = {
	"1": "Monday",
	"2": "Tuesday",
	"3": "Wednesday",
	"4": "Thursday",
	"5": "Friday",
	"6": "Saturday",
	"7": "Sunday"
}

def day(num):
	if int(num) < 1 or int(num) > 7:
		print("\nPlease enter a number between 1 and 7\n")
        day(num)
	else:
		print("\n" + days[num] + "\n")
		
day(num)




