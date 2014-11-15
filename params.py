def calculate(radius, choice):
        pi = 3.14159

        if choice == 1:
            area = pi * radius ** 2
            print("The area is ", area)
        elif choice == 2:
            diam = radius * 2
            print("The diameter is ", diam)
        else:
            circ = 2 * pi * radius
            print("The circumference is ", circ )
    

def main():

    torepeat = 'y'
    while torepeat != 'q':
        radius = float(input("Enter the radius of a circle: "))
        while radius < 0:
            radius = float(input("Radius cannot be negative. Try again: "))
                  
        choice = int(input("Enter\n1 to calculate area or\n2 to calculate diameter or\
            \n3 to calculate  circumference\n"))
        while choice > 3 or choice < 1:
            choice = int(input("Choice has to have a value 1, 2, or 3. Try again: "))

        calculate(radius, choice)
        
        print('Do you want to repeat the program or quit?')
        torepeat = input('Enter q to quit, or any other character to continue: ')

main()