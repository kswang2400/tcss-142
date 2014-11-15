


num = int(input("What is the number? "))

repeat = True
count = 0
tracker = []

while repeat is True:
	count += num % 10
	tracker.append(count)
	num = int(num / 10)
	if num == 0:
		repeat = False

print(tracker)
print(count)

