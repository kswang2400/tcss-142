import datetime

def main():
	amazonList = []
	appleList = []

	with open('amazonstock.csv', 'r') as amazon:
		amazon.readline()
		for line in amazon:
			amazonList.append(line.strip().split(','))

	with open('applestock.csv', 'r') as apple:
		apple.readline()
		for line in apple:
			appleList.append(line.strip().split(','))

	indexAmazon = 0
	indexApple = 0
	# while indexAmazon < len(amazonList) or indexApple < len(appleList):
	# 	amazonDate = amazonList[indexAmazon][0].split('-')
	# 	appleDate = appleList[indexApple][0].split('-')
		# dateAmazon = datetime.date(int(amazonDate[0]), int(amazonDate[1]), 
		# 	int(amazonDate[2]))
		# dateApple = datetime.date(int(appleDate[0]), int(appleDate[1]), 
		# 	int(appleDate[2]))

	# if dateAmazon == dateApple:
	# 	indexAmazon += 1
	# 	indexApple += 1
	# elif dateAmazon < dateApple:
	# 	del(appleList[indexApple])
	# else:
	# 	del(amazonList[indexAmazon])

if __name__ == '__main__':
	main()