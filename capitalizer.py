

def main():
	sentence = input("Sentence: ")
	sentence = sentence.capitalize()
	for i, char in enumerate(sentence):
		print("i", i, "char", char)
		if char in '.!?':
			sentence = sentence[:i+2] + sentence[i+2:].capitalize()
	
	print(sentence)

main()

