#Time To Run: 0.835687875748 seconds
import math
import time
def addDigits(number):
	number = list(str(number))
	#print number
	sum = 0
	for i in number:
		if i == '.':
			break
		sum+=long(i)
	return sum
def calcHugePower(max):
	highest = 0
	for i in range(0, max):
		for k in range(0, max):
			sum = addDigits(pow(i, k))
			if(sum>highest):
				highest = sum
	return highest
start_time = time.time()
print calcHugePower(100)	
print("--- %s seconds ---" % (time.time() - start_time))
