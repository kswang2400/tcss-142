# Find the average age of five people around you
# using integer division and floating point division

sum = 29 + 21 + 18 + 18 + 21
averageInt = sum // 5
averageFlt = sum / 5

# Compute 2 ^ 10

expInt = 2 ** 10

# Compute 2.0 ^ 10

expFlt = 2.0 ** 10

# Compute the factorial of 5

import math
fact = math.factorial(5)

# Compute the number of seconds in a year

seconds = 365 * 24 * 60 * 60

# Print statements

print("Average age = " + str(averageInt) + " or " + str(averageFlt))
print("2 ^ 10 = " + str(expInt))
print("2.0 ^ 10 = " + str(expFlt))
print("The factorial of 5 = " + str(fact))
print("The number of seconds in a year is " + str(seconds))



import sys
print(sys.float_info)

print(2 + 3 * 4 - 6)
print((2 + 3) * 4 - 6)
print(4.0 / 2 * 9 / 2)
print(4.0 / (2 * 9) / 2)
print(4 / (2 * 9) / 2)
print(7 % 2)
print(12 % 100)
print(813 % 100)
print(813 % 100 + 2)
