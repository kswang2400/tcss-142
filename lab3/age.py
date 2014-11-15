age = int(input("What is your age? "))

# if age >= 21:
# 	print("Guess what - you can drink alcohol")
# if age >= 18:
# 	print("And you can also vote or join the military")
# if age >= 16:
# 	print("You are eligible to drive")
# else:
# 	print("Stay in school")

output = ""

if age >= 21:
	output = "Guess what - you can drink alcohol"
if age >= 18:
	output = "and you can also vote or join the military. " + output
if age >= 16:
	output = "You are eligible to drive " + output
else:
	print("Stay in school")

print("")
print(output)
print("")

# assume a, x, y etc are properly initiated

# if a == 1:
# 	print(a)
# 	x = a ** 1
# 	y = y * 2
# elif a == 2:
# 	print(a)
# 	x = a ** 2
# elif a < 1 or a > 2:
# 	print(a)
# 	x = a ** a

# print(a)
# x = a ** a
# if a == 1:
# 	y += 2