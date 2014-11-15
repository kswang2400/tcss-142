'''
Lab 7
Kevin Wang
11/12/14
'''

import re

#3 Strings and Functions

'''capitalizer'''

def capitalizer():
	sentence = input("\nSentence for capitalizing: ")
	sentence = sentence.capitalize()
	for i, char in enumerate(sentence):
		if char in '.!?':
			sentence = sentence[:i+2] + sentence[i+2:].capitalize()
	print('\n', sentence, '\n')
	return sentence

'''splitter'''

def splitter():
	sentence = input("Sentence for split: ")
	lst = [a for a in re.split(r'([A-Z][a-z]*)', sentence) if a]
	print('\n', " ".join(lst), '\n')

'''insert'''

def insert():
	string = input("Main string: ")
	index = int(input("Index: "))
	char = input("Character for inserting: ")
	if index < 0 or index > len(string):
		return string
	newString = string[:index] + char + string[index:]
	print('\n', newString, '\n')
	return newString

#4 Problem Solving with Strings and Functions

def main():
    input("Press enter to continue")
    cipherText = encrypt('123456')   
    print("Transposition cipher: ", cipherText)
    plain = decrypt(cipherText)
    print("Checking our decryption: ", plain)
    cipherText = encrypt('12345')   
    print("Transposition cipher: ", cipherText)
    plain = decrypt(cipherText)
    print("Checking our decryption: ", plain)
    cipherText = encrypt('1234')   
    print("Transposition cipher: ", cipherText)
    plain = decrypt(cipherText)
    print("Checking our decryption: ", plain)


def encrypt(string):
	cipher = ""
	for i in range(2, len(string), 3):
		cipher += string[i]
	for i in range(1, len(string), 3):
		cipher += string[i]
	for i in range(0, len(string), 3):
		cipher += string[i]
	return cipher

def decrypt(string):
	mapping = {}
	position = []
	for i in range(2, len(string), 3):
		position.append(i)
	for i in range(1, len(string), 3):
		position.append(i)
	for i in range(0, len(string), 3):
		position.append(i)

	for i in range(len(string)):
		mapping[position[i]] = string[i]

	plainList = mapping.values()
	return "".join(plainList)

capitalizer()
splitter()
insert()
main()

