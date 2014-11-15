input("Press Enter to continue")

def main():
	animalNoise = []

	bought("cat", animalNoise)
	bought("hen", animalNoise)
	bought("duck", animalNoise)
	bought("goose", animalNoise)
	bought("sheep", animalNoise)
	bought("fox", animalNoise)

def bought(animal, animalNoise):
	print("Bought me a {} and the {} pleased me,".format(animal, animal))
	print("I fed my {} under yonder tree.".format(animal))

	if animal == "cat":
		animalNoise.append("Cat goes fiddle-i-fee.\n")
	elif animal == "hen":
		animalNoise.append("Hen goes chimmy-chuck, chimmy-chuck,")
	elif animal == "duck":
		animalNoise.append("Duck goes quack, quack,")
	elif animal == "goose":
		animalNoise.append("Goose goes hissy, hissy,")
	elif animal == "sheep":
		animalNoise.append("Sheep goes baa, baa,")
	elif animal == "fox":
		animalNoise.append("""What a minute - What does the fox say?
Ring-ding-ding-ding-dingeringeding?
Wa-pa-pa-pa-pa-pa-pow?
Hatee-hatee-hatee-ho?
Joff-tchoff-tchoff-tchoffo-tchoffo-tchoff?
			""")
	for x in reversed(animalNoise):
		print(x)

main()