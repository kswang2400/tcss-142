
def main():
	earthquake = createListMag()
	# print(earthquake)
	summary(earthquake)

def createListMag():
	listMag = []
	with open('earthquake.txt') as dataset:
		for line in dataset:
			mag = line[5:8]
			listMag.append(mag)
	listMag.remove('  \t')
	listMag.sort()
	return listMag

def mean1(lst):
	count = 0
	total = 0
	for n in lst:
		count += 1
		total += float(n)
	return (total / count)

def median1(lst):
	length = len(lst)
	half = int(length / 2)
	if length % 2 == 0:
		median = (float(lst[half]) + float(lst[half-1])) / 2
	else:
		median = lst[half]
	return median

# def minimum(lst):
# 	minimum = lst[0]
# 	for i in lst:
# 		if i < minimum:
# 			minimum = i

def summary(lst):
	minimum = lst[0]
	maximum = lst[-1]
	rangelst = '({}, {})'.format(minimum, maximum)
	mean = round(mean1(lst), 2)
	median = median1(lst)
	print('\nMin:', minimum)
	print('Max:', maximum)
	print('Range:', rangelst, round(float(maximum) - float(minimum), 2))
	print('Mean:', mean)
	print('Median:', median, '\n')

if __name__ == '__main__':
	main()

