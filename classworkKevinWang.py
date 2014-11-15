# chapter 2 pg 77 2, 3, 5, 7, 9

#2
sales = float(input("What are the annual sales? "))
profit = round(sales * 0.23, 2)
print("Profit = " + str(profit))

#3
sFeet = int(input("How many square feet? "))
acres = round(sFeet / 43560, 2)
print("Acres = " + str(acres))

#5
speed = int(input("How many miles per hour? "))
print("The distance traveled in 5 hours = " + str(speed * 5))
print("The distance traveled in 8 hours = " + str(speed * 8))
print("The distance traveled in 12 hours = " + str(speed * 12))

#7
miles = int(input("How many miles driven? "))
gallons = int(input("How many gallons used? "))
mpg = round(miles/ gallons, 2)
print("MPG = " + str(mpg))

#9
c = int(input("Celsius: "))
fahr = round((9 * c) / 5 + 32, 2)
print("Fahrenheit: " + str(fahr))

###############################
# chapter 3 pg 115 1, 3, 6, 10, 12-15

#1
num = input("Enter a number from 1 to 7: ")

days = {
	"1": "Monday",
	"2": "Tuesday",
	"3": "Wednesday",
	"4": "Thursday",
	"5": "Friday",
	"6": "Saturday",
	"7": "Sunday"
}

def day(num):
	if int(num) < 1 or int(num) > 7:
		print("\nPlease enter a number between 1 and 7\n")
		num = input("Enter a number from 1 to 7 ")
		day(num)
	else:
		print("\n" + days[num] + "\n")
		
day(num)

#3
age = int(input("Age: "))

if age < 0:
	print("Please enter a positive age.")
elif age < 1:
	print("Infant")
elif age < 13:
	print("Child")
elif age < 20:
	print("Teenager")
else: 
	print("Adult")

#6



#10











