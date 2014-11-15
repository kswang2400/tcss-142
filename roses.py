def rhyme(flower1 = "Roses", color1 = "red", flower2 = "Violets", color2 = "blue"):
    print(flower1, "are", color1)
    print(flower2, "are", color2)
    print("I'm a bad poet")
    print("but so are you")

rhyme()
rhyme("Daisies", "white")  # left matching
rhyme(flower2 = "Tulips")
rhyme(flower2 = "Irises", color1 = "yellow")
rhyme("Lilies", color1 = "purple")
print(rhyme())


