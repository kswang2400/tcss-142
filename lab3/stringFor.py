
string = input("What is your string? ")
count = 0

for ch in string.upper():
	# print(ch)
	if ch == "I":
		count += 1

print(count)

### transposition Cipher

original = input("What is your string? ")
even = ""
odd = ""


for i, ch in enumerate(original):
	if i % 2 == 0:
		even = even + ch
	else:
		odd = odd + ch

print("")
print("Even = " + even)
print("Odd = " + odd)
print("")