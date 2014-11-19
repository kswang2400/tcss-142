
def main():
	outputPigL = open("outputPigL.txt", "w")
	with open('myPigLatinTest.txt') as text:
		for line in text:
			listWords = line.split(" ")
			if '\n' in listWords:
				listWords.remove('\n')
			print(listWords)
			pigLine = " ".join(pigLatin(listWords))
			print(pigLine)
			outputPigL.write(pigLine + '\n')

def pigLatin(alist):
	pigList = []
	vowels = 'AEIOUaeiou'
	for word in alist:
		if word[0] in vowels:
			newWord = word + 'way'
		else:
			newWord = word[1:] + word[0] + 'ay'
		pigList.append(newWord)
	return pigList

if __name__ == "__main__":
	print("")
	main()
	print("")