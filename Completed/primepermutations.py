#Time To Run: 24.7911250591 seconds
import math
import time
def generatePrimes(under):
	primes = [2]
	i = 3
	while(i<under):
		#print(i)
		for k in primes:
			if(i%k==0):
				break
			if(k>math.sqrt(i)):
				#print("Should add")
				primes.append(i)
				break
		#print(i)
		i+=2
	#print len(primes)
	print("Done Generating primes")
	return primes
def findSets():
	primes = generatePrimes(9994)
	for i in primes:
		if i < 1000:
			continue
		if i == 1487:
			continue
		for k in range(1,3333):
			if (k+i) in primes:
				#print("1")
				if (k+k+i) in primes:
					#print("2")
					if checkPermutations(i,(k+i),(k+k+i)):
						return str(i)+str((k+i))+str((k+k+i))
	return "NONE FOUND"
def checkPermutations(int1,int2,int3):
	avalibleDigits = list(str(int1))
	#print avalibleDigits
	for i in list(str(int2)):
		if i in avalibleDigits:
			avalibleDigits.remove(i)
	if len(avalibleDigits)>0:
		return False
	avalibleDigits1 = list(str(int1))
	for i in list(str(int3)):
			if i in avalibleDigits1:
				avalibleDigits1.remove(i)
	if len(avalibleDigits1)!=0:
		return False
	return True
start_time = time.time()
print findSets()
print("--- %s seconds ---" % (time.time() - start_time))	
