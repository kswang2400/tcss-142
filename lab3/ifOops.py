val1 = int(input("Enter a value: "))
print("You entered: ", str(val1)) 		# str() not necessary
print("")

val2 = int(input("Enter another value: "))
print("You've entered: ", str(val2))
print("")

if val1 <= val2:
	print("The first value is smaller or equal to the second one")
else:
    print("The first value is larger")
print("Have a nice day!")

print("this is a string" , 3)