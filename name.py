
class Name:

	def __init__(self, first, middle, last):
		self.__first = first
		self.__middle = middle
		self.__last = last

	def __str__(self):
		return "({} {} {})".format(self.__first, self.__middle, self.__last)

	def getReverseOrder(self):
		return "{}, {} {}".format(self.__last, self.__first, self.__middle)

	def setFirst(self, first):
		self.__first = first
		
	def setMiddle(self, middle):
		self.__middle = middle

	def setLast(self, last):
		self.__last = last

	def getFirst(self):
		return self.__first

	def getMiddle(self):
		return self.__middle

	def get Last(self):
		return self.__last

def main():
	kevin = Name('Kevin', 'S.', 'Wang')
	print(kevin)
	print(kevin.getReverseOrder())

if __name__ == '__main__':
	main()