
a = input("string1: ")
b = input("string2: ")

def anagram(string1, string2):
	lst1 = list(string1)
	lst1.sort()
	lst2 = list(string2)
	lst2.sort()
	return (lst1 == lst2)

print(anagram(a, b))