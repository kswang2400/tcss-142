
# 2. Adding outer loops

### transposition.py repeat until 'N'

repeat = True

while repeat is True:
	string = input("What is your string? ")

	even = ""
	odd = ""

	for i, x in enumerate(string):
		if i % 2 == 0:
			odd += x
		else:
			even += x

	print(string)
	print(even)
	print(odd)

	repeat = input("Do you want to repeat? (Y/N) ")
	if repeat != 'N':
		repeat = True

### gangsta.py repeat three times

for x in range(3):
	name = input("What is your name? ")

	firstName = ""
	lastName = ""
	switch = False

	for ch in name:
		if ch == " ":
			switch = True
		elif switch == False:
			firstName = firstName + ch
		elif switch == True:
			lastName = lastName + ch

	gangsta = firstName[0].upper() + ". Diddy " + lastName + " " + firstName + "-izzle"
	print(gangsta)

# 3. Nested loops

# 4. Problem solving with nested loops

input("Enter to continue\n")
for n in range(1, 8):
	print(str(n) * 7)
print("")

input("Enter to continue\n")
for n in range(1, 8):
	print(str(n) * n)
print("")

### Rainfall

weeks = int(input("Number of weeks: "))
totalRainfall = 0

for x in range(weeks):
	for i in range(7):
		daily = float(input("Enter the rainfall for day {}	".format(i)))
		totalRainfall += daily

averageRainfall = round(totalRainfall / weeks, 1)
totalRainfall = round(totalRainfall, 1)

print("Number of weeks:", weeks)
print("Total rainfall:", totalRainfall)
print("Average rainfall:", averageRainfall)







