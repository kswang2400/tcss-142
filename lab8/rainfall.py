
def main():
	print("")
	myFile = open('rainfall.txt', 'r')
	sub = 'had'
	sub2 = 'inches of rain'
	for line in myFile:
		line = line.split()
		print(line[0] + " " + sub + " " + line[1] + " " + sub2)
	print("")
	myFile.close

if __name__ == "__main__":
	main()