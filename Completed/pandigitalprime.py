#Time to Run: 0.00427103042603 seconds
import math
import time
def pDPrimes():
	for i in xrange(7654321,1, -2):
		if isPandigital(i):
			#print i
			if isPrime(i):
				return i
def isPrime(num):	
	if num%2==0 or num%5==0:
		return False
	for i in xrange(3,int(math.ceil(math.sqrt(num)))+1,2):
		if num%i==0:
			return False
	return True
def isPandigital(num):
	num = list(str(num))
	for i in num:
		if num.count(i)>1:
			return False
	for i in range(1,len(num)+1):
		if num.count(str(i))!=1:
			return False
	return True
start_time = time.time()
print pDPrimes()
print("#Time to Run: %s seconds" % (time.time() - start_time))
#print isPandigital(1234)
