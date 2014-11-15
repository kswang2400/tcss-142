'''
142 Midterm Study Guide
Kevin Wang
'''

from random import randint

# 3. If statements

ticket = int(input("What is the cost of the ticket? "))
stars = int(input("What is the number of stars? "))

def interest(ticket, stars):
	if ticket < 5:
		print("very interested")

	if ticket >= 12:
		if stars == 5:
			print("sort-of interested")
		else: 
			print("not interested")

	if 5 <= ticket < 12:
		if 2 <= stars <= 4:
			print("sort-of interested")
		else:
			print("not=interested") 

interest(ticket, stars)

# 4. For loops

count = 0

for x in range(10):
	num = 2 ** x
	count += num

print(count)
average = count/10
print("Average: ", average)

lowBound = int(input("Where do start? "))
terms = int(input("How many terms? "))

count = 0
for x in range(terms):
	num = lowBound * 2 ** x
	count += num

print(count)
average = count/terms
print("Average: ", average)

# 5. While loops

x= 1
while x < 100:
	print(x)
	x += 10 		# should print 1, 11, 21, 31 ... 91 (10 times)

y = 10
while y < 10:
	print("count down: ", y)
	y = y -1 		# zero times, y does not start less than 10

z = 250
while z % 3 != 0:
	print(z)		# infinite times, 250 % 3 != 0, no changes to z are made
	break

# Pythonian half-life

def decay(amount, rate):
	newAmount = amount * (1 - rate/100)
	return newAmount

amount = int(input("How much Pythonian? "))
rate = float(input("Rate of decay? "))

half = amount / 2

print("\nInput original mass:", amount)
print("Year		Mass")
year = 0
while amount >= half:
	amount = decay(amount, rate)
	year += 1
	print("{}		{}".format(year,amount))

# coin flip, three heads in a row

def flip():
	flip = randint(1, 2)
	if flip == 1:
		coin = "H"
	else:
		coin = "T"
	return coin

def threeInRow():
	results = []
	counter = 0
	while counter < 3:
		HT = flip()
		results.append(HT)
		# print(results)
		if HT == "H":
			counter += 1
			# print("counter", counter)
		else:
			counter = 0

	print(results)
	print("Congrats, three H in a row!")

threeInRow()

