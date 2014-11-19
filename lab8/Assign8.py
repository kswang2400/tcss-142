'''
Lab 8
Kevin Wang
11/19/14
'''

# 3 Lists and Functions

def largerThan(alist, num):
	larger = []
	for n in alist:
		if n > num:
			larger.append(n)
	return larger

def numDistinct(alist):
	simpleList = []
	unique = []
	for n in alist:
		if n not in unique:
			simpleList.append(n)
			unique.append(n)
	return simpleList

def normalizeList(alist):
	for i, n in enumerate(alist):
		if n <= 0:
			alist[i] = 0
		elif n >= 100:
			alist[i] = 100
	return alist

# 4 Problem solving with lists, strings, functions and files

def readWritePL():
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
	print(largerThan([1, 2, 4, 2, 7], 2))
	print(numDistinct([1, 2, 4, 2, 7]))
	print(normalizeList([0, 35, -23, 100, 200]))
	readWritePL()



