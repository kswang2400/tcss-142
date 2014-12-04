'''
Lab 10
Kevin Wang
12/3/14
'''

# 2 File Reading

def readFile():
	input("\nPress enter to continue\n")
	f = input("Name of file (example: test2a1): ")

	with open('{}.txt'.format(f), 'r') as dataset:
		n = 0
		lines = dataset.readlines()

		while n <= 4:
			if n > len(lines) - 1:
				break
			print(lines[n])
			n += 1

	dataset.close()

def houseSummary():
	input("\nPress enter to continue\n")
	houseSummary = open('houseSummary.csv', 'w')
	houseSummary.write('Listing,Price,Size(sqft),Number of Rooms\n\n')

	houseDict = {}

	with open ('houseData.csv', 'r') as dataset:
		next(dataset)
		for line in dataset:
			wordList = []
			for word in line.split(','):
				wordList.append(word)
			wordList[-1] = wordList[-1].strip('\n')
			houseDict[tuple(wordList[:2])] = wordList[2:]

	for listing in houseDict:
		sizeHouse = 0
		numRooms = len(houseDict[listing])

		for room in houseDict[listing]:
			sizeHouse += int(room)

		houseInfo = '{},{},{},{}\n'.format(listing[0], listing[1], sizeHouse, numRooms)
		houseSummary.write(houseInfo)

	dataset.close()
	houseSummary.close()
	print('\nProcessing Complete\n')

# List of lists

def total(matrix):
    t = 0
    for el in matrix:
        t += sum(el)
    return t

def rowAverage(matrix):
    for i in range(len(matrix)):
        ave = sum(matrix[i]) / len(matrix[i])
        print("average for row ", i, " is ", ave)

def replace(matrix, row):
    for col in range(len(matrix[row])):
        matrix[row][col] = 0

def addValue(matrix, value):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] += value

def buildMatrix(rows, columns, value):
    newM = []
    for i in range(rows):
        rowList = []
        for j in range(columns):
            rowList.append(value)
            value += 1
        newM.append(rowList)
    return newM
    
def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    
    input("\nPress enter to continue\n")
	
    print("the sum of matrix is: ", total(matrix))
    rowAverage(matrix)
    replace(matrix, 1)
    print(matrix)
    addValue(matrix, 1)
    print(matrix)
    print(buildMatrix(4, 5, 0), '\n')

if __name__ == '__main__':
	readFile()
	readFile()
	houseSummary()
	main()




