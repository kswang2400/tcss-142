
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
	if repeat == N:
		repeat = False

