for i in range(1, 5):
	print(i, "potato")

#### pattern.py

length = int(input("How long? "))

line1 = ""
line2 = ""
line3 = ""
for x in range(length):
	line1 += "/\\"
	line2 += "||"
	line3 += "\\/"

print(line1)
print(line2)
print(line3)

print("")
print("/\\" * 20)
print("||" * 20)
print("\\/" * 20)

count1 = 0
count2 = 0
count3 = 0
count4 = 0

start = int(input("Where to start? "))
stop = int(input("Where to end? "))
step = int(input("What is the step-size "))

for i in range(start, stop + 1, step):
	print(i)
	count1 += i
print("")
for i in range(14, 25, 2):
	print(i)
	count2 += i
print("")
for i in range(6, 31, 3):
	print(i)
	count3 += i
print("")
for i in range(7, -8, -2):
	print(i)
	count4 += 1

print("")
print(
	count1, count2, count3, count4
	)
print("")


