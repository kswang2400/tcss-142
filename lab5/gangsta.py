	
counter = 0

while counter != 3:
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
	count += 1