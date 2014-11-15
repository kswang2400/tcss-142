
num = int(input("Enter a number (0 to quit): "))
counter = num

while num != 0:
	num = int(input("Enter a number (0 to quit): "))
	counter += num
	if num == 0:
		print("The sum is ", counter)
		repeat = False