originalName = input("Type your name: ")
print(originalName)

spaceIndex = originalName.find(' ')
firstName = originalName[:spaceIndex]
lastName = originalName[spaceIndex+1:]
begin = originalName[0]+". Diddy"
    
gangstaName = begin + ' ' + lastName + ' ' + firstName + "-izzle"

print("Gangsta Name: ", gangstaName)
    
