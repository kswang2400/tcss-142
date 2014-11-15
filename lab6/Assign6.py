'''
Assignment 6
Kevin Wang
11/5/14
'''

# 2. Functions 1
input("\nPress Enter to continue\n")

def main1():
  bubble = 867.5309
  x = 10.01
  y = 8.0
  z = 5
  printer(x, y)
  y = bubble
  printer(x, y)
  print("The value from main is:", bubble)
  print("z =", z)

def printer(x, y):
  print("x = ", x, " and y = ", y)
  
main1()

# 3. Functions 2
input("\nPress Enter to continue\n")

def bought(animal):
	global animalNoise
	print("Bought me a {} and the {} pleased me,".format(animal, animal))
	print("I fed my {} under yonder tree.".format(animal))

	if animal == "cat":
		animalNoise = "Cat goes fiddle-i-fee.\n" 
	elif animal == "hen":
		animalNoise = "Hen goes chimmy-chuck, chimmy-chuck,\n" + animalNoise
	elif animal == "duck":
		animalNoise = "Duck goes quack, quack,\n" + animalNoise
	elif animal == "goose":
		animalNoise = "Goose goes hissy, hissy,\n" + animalNoise
	elif animal == "sheep":
		animalNoise = "Sheep goes baa, baa,\n" + animalNoise
	elif animal == "fox":
		animalNoise = """What a minute - What does the fox say?
Ring-ding-ding-ding-dingeringeding?
Wa-pa-pa-pa-pa-pa-pow?
Hatee-hatee-hatee-ho?
Joff-tchoff-tchoff-tchoffo-tchoffo-tchoff?
			"""
	print(animalNoise)

global animalNoise
animalNoise = ""

bought("cat")
bought("hen")
bought("duck")
bought("goose")
bought("sheep")
bought("fox")


input("Press Enter to continue")

def main2():
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

main2()


# 4. Rock Paper Scissors
input("\nPress Enter to continue\n")
from random import randint

def main3():
    repeat = True
    while repeat:
        user = input("Pick rock, paper or scissors: ").lower()
        comp = computer()
        repeat = game(user, comp)


def game(user, computer):
    print("You picked {}".format(user))
    print("Computer picked {}".format(computer))

    if user == "rock":
        if computer == "paper":
            print("You lose, paper beats rock")
        elif computer == "scissors":
            print("You win!")
        else:
            print("You picked the same, try again")
    elif user == "paper":
        if computer == "rock":
            print("You win!")
        elif computer == "scissors":
            print("You lose, scissors beats paper")
        else:
            print("You picked the same, try again")
    elif user == "scissors":
        if computer == "paper":
            print("You win!")
        elif computer == "rock":
            print("You lose, rock beats scissors")
        else:
            print("You picked the same, try again")
    else:
    	print("You didn't pick rock, paper or scissors")

    
    repeat = input("Play again? Y/N ").upper()
    if repeat == "N":
        return False
    else:
        return True

def computer():
    num = randint(1, 3)
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "scissors"

main3()
