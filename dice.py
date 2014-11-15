from random import randint, seed

seed()
result = 0
counter = 0

while result != 7:
	roll1 = randint(1, 6)
	roll2 = randint(1, 6)
	result = roll1 + roll2 
	print("{} + {} = {}".format(roll1, roll2, result))
	counter += 1 

print(counter)

