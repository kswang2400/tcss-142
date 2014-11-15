def main():
	string = input("What is your string? ")
	cipherText = encrypt(string)
	print("Cipher =", cipherText)


def encrypt(string):
	even = ""
	odd = ""

	for i, x in enumerate(string):
		if i % 2 == 0:
			odd += x
		else:
			even += x

	cipherText = odd + even
	return cipherText

main()
