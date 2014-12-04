from point import Point

def main():
	myClass = Point()
	newPoint = Point()
	print("Point:", myClass)
	myClass.setLocation(4, 3)
	print("Distance:", myClass.distance(newPoint))
	print("Translate:", myClass.translate(2, 2))
	print(myClass.flip())

if __name__ == "__main__":
	main()