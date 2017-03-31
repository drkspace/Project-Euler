#Time To Run: 2.72225999832 seconds
import math
import time
def calcAndCheck(bound):
	distinctPow = [0]
	for i in range(2, bound+1):
		for k in range(2, bound+1):
			#print k
			power = math.pow(i, k)
			#print power
			if inList(distinctPow, power) == False:
				distinctPow.append(power)
				
	return len(distinctPow)-1

def inList(alist, aValue):
	for i in alist:
		if aValue==i:
			return True
	return False
start_time = time.time()
print calcAndCheck(100)
print("--- %s seconds ---" % (time.time() - start_time))
