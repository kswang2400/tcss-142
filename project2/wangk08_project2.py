'''
Project 2
Kevin Wang
11/26/14
'''

from collections import OrderedDict

def main():
	statsFile = input("Name of txt file to write to (example: stats1): ")
	quakeFile = input("Name of txt file to read earthquake data (example: earthquake1): ")
	
	earthquakeDict = genEarthquakeDict(quakeFile)
	writeFile(earthquakeDict, statsFile)
	writeSummary(earthquakeDict)

def genEarthquakeDict(quakeFile):
	earthquakeDict = {}

	with open('{}.txt'.format(quakeFile)) as dataset:
		next(dataset)
		for line in dataset:
			wordList = []
			for word in line.split():
				wordList.append(word)

			strength = classify(float(wordList[1]))
			region = ' '.join(wordList[7:])

			if region not in earthquakeDict:
				earthquakeDict[region] = [0] * 5

			if strength:
				if strength == 'Moderate':
					earthquakeDict[region][0] += 1
				elif strength == 'Strong':
					earthquakeDict[region][1] += 1
				elif strength == 'Major':
					earthquakeDict[region][2] += 1
				elif strength == 'Great':
					earthquakeDict[region][3] += 1
				earthquakeDict[region][4] += 1

	return earthquakeDict

def writeFile(earthquakeDict, statsFile):
	output = open('{}.csv'.format(statsFile), 'w')

	output.write('REGION,MODERATE,STRONG,MAJOR,GREAT,OVERALL\n\n')

	for region in sorted(earthquakeDict.keys()):
		if not earthquakeDict[region] == [0] * 5:
			stringOutput = '"{0}",{1[0]},{1[1]},{1[2]},{1[3]},{1[4]}\n'.format(region, earthquakeDict[region])
			output.write(stringOutput)

def writeSummary(earthquakeDict):
	summary = open('summary.txt', 'a')

	totalQuakes = 0
	maxQuakes = 0
	for region in sorted(earthquakeDict.keys()):
		if not earthquakeDict[region] == [0] * 5:
			totalQuakes += earthquakeDict[region][4]
			if earthquakeDict[region][4] > maxQuakes:
				maxQuakes = earthquakeDict[region][4]
				regionMax = region

	summary.write('\nTotal number of quakes: {}\n'.format(totalQuakes))
	summary.write('\nRegion with the highest number of earthquakes: {}\n'.format(regionMax))

	print('Processing Complete')
	summary.close()

def classify(magnitude):
	magnitude = float(magnitude)
	if magnitude >= 8:
		return 'Great'
	elif magnitude >= 7:
		return 'Major'
	elif magnitude >= 6:
		return 'Strong'
	elif magnitude >= 5:
		return 'Moderate'

if __name__ == '__main__':
	main()

	