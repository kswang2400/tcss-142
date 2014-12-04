import urllib.request

def main():
	page = urllib.request.urlopen('http://faculty.washington.edu/monikaso')
	headCounter = 0
	countHead = False

	bodyCounter = 0
	countBody = False

	for pageText in page:
		pageText = str(pageText)

		if "</head>" in pageText:
			countHead = False
		if countHead:
			headCounter += 1
		if "<head>" in pageText:
			countHead = True

		if "</body>" in pageText:
			countBody = False
		if countBody:
			bodyCounter += 1
		if "<body" in pageText:
			countBody = True

	print('head', headCounter)
	print('body', bodyCounter)

if __name__ == "__main__":
	main()