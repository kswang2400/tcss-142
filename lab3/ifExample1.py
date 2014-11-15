pi = 3.14159
radius = float(input("Enter the radius of a circle: "))
choice = int(input("Enter\n1 to calculate area or\n2 to calculate diameter or\
    \n3 to calculate  circumference\n"))

if choice == 1:
	area = pi * (radius ** 2)
	print("Area = " + str(area))
elif choice == 2:
	diameter = 2 * radius
	print("Diameter = " + str(diameter))
elif choice == 3:
	circumference = 2 * pi * radius
	print("Circumference = " + str(circumference))
else:
	print("Please enter 1, 2, or 3")
