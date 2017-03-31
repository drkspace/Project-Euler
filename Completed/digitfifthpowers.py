#Time to run: 16.8404929638 seconds
import math
import time
def addDigits5(number):
	hold = number
	number = list(str(number))
	#print number
	sum = 0
	for i in number:
		if i == '.':
			break
		sum+=pow(long(i),5)
	if sum == hold:
		return sum	
	else: 
		return 0
def calcUnder(under):
	sum = 0
	for i in range(10,under):
		sum += addDigits5(i)
		
	return sum
start_time = time.time()
print calcUnder(1000000)
print("--- %s seconds ---" % (time.time() - start_time))	
