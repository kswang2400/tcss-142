

def main():
	s = input("Enter a list of numbers separated by spaces: ").split()
	lst = []
	for n in s:
		lst.append(int(n))
	halfLength = int(len(lst)/2)


	if len(lst) % 2 == 0:
		median = (float(lst[halfLength]) + float(lst[halfLength-1])) / 2
	else:
		median = lst[halfLength]

	print(median)
	return median

main()