from math import sqrt

class Point():

	def __init__(self, x = 0, y = 0):
		self.__x = x
		self.__y = y

	def getLocation(self):
		return self.__x, self.__y

	def setLocation(self, x, y):
		self.__x = x
		self.__y = y
		return

	def translate(self, dx, dy):
		newX = self.__x + dx
		newY = self.__y + dy
		return (newX, newY)

	def distance(self, secondPoint):
		x, y = secondPoint.getLocation()
		dx = self.__x = x
		dy = self.__y = y 
		distance = sqrt(dx ** 2 + dy ** 2)
		return distance

	def flip(self):
		temp = self.__x
		self.__x = self.__y
		self.__y = temp
		return (self.__x, self.__y)

	def __str__(self):
		return "({}, {})".format(self.__x, self.__y)

def main():
	myClass = Point()
	print("Point:", myClass)
	myClass.setLocation(4, 3)
	print("Distance:", myClass.distance(7, 7))
	print("Translate:", myClass.translate(2, 2))
	print(myClass.flip())

if __name__ == "__main__":
	main()