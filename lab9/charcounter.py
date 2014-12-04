
def main():
	myFile = open("file.txt", "r")
	charCount = [0] * 26

	zero = ord('A') 				# 65
	for line in myFile:
		for ch in line.upper():
			val = ord(ch) - zero
			if 0 <= val < 26:
				charCount[val] += 1
	print('charCount:', charCount)

	for i in range(26):
		print('{}: {}'.format(chr(zero + i), charCount[i]))
	return charCount


if __name__ == "__main__":
	main()
