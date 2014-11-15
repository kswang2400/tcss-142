
def main():
	repeat = 'n'
	
	while repeat != 'q':
		repeat = calculate()

	print("good job, you're done")

def calculate():

	radius = int(input("Enter the radius of a circle: "))
	choice = int(input("Enter\n1 to calculate area. \n2 to calculate diameter \
	\n3 to calculate circumference\n Choice: "))

	pi = 3.14159
	area = pi*radius**2
	diameter = 2*radius
	circum = 2*pi*radius


	while radius < 0:
		radius = float(input("radius cannot be negative. try again."))

	while choice > 4 or choice < 0:
		choice = int(input('Choice has to have a value 1 2 or 3, try again: '))

	if choice == 1:
		print("The area of the circle is ", area, '.' ,sep="")
	elif choice == 2:
		print("The diameter is ", diameter, '.' ,sep="")
	elif choice == 3:
		print("The circumference is ", circum, '.' ,sep="")
	elif choice == 3:
		print("This is a second choice")
	else:
		print("Invalid choice.")
	
	repeat = input('Continue? (q to quit): ')
	return repeat


main()
