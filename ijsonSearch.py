import ijson
import sys
import time

tStart = time.time()

fileName = sys.argv[1]
targetCat = sys.argv[2]
target = sys.argv[3]

def searchJson(cat , targetName):
	f = open(fileName)
	print("loading json")
	objects = ijson.items(f, 'item')
	print("loading done")
	count = 0
	for article in objects:
		count+=1
		if article[cat] == targetName:
			print(article)
			break;
	print("count: " + str(count))

if targetCat == 'i':
	searchJson("id" , target)
elif targetCat == 't':
	searchJson("title" , target)

tEnd = time.time()
print ("It cost %f sec" % (tEnd - tStart))