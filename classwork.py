 
l = [1]
answer = True

while answer is True:
	if l[0] == 1:
		num = int(input("Enter a number: "))
		l[0] = num
		print("Sorted")
		print(l)
	elif num != l[-1] + 1:
		answer = False
		print("Not sorted")
	else:
		num = int(input("Enter a number: "))
		l.append(num)
		print("Sorted")
		print(l)

