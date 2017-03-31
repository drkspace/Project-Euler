#Time To Run: 8.71173000336 seconds

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
Consecutive prime sum
def circularPrimes(under):
	primes = generatePrimes(under)
	count = 4
	brk = False
	for k in primes:
		correctHits = 0
		number = list(str(k))
		if '2' in number:
			 continue
		if '4' in number:
			 continue
		if '6' in number:
			 continue
		if '8' in number:
			 continue
		if '5' in number:
			 continue
		if '0' in number:
			 continue
		length = len(number)
		if length!=1:		
			for i in range(0, length+1):
				tmp = number[0]
				i = 0
				while i < length-1:
					#print number
					number[i]=number[i+1]
					i+=1
				number[length-1]=tmp
				#print number
				toCheck = map(str, number)
				toCheck = ''.join(toCheck)
				toCheck = int(toCheck)
				if inList(primes, toCheck):
					correctHits+=1
					#print(toCheck)
				else:
					brk=True
					break
			if brk:
				brk = False		
			else:
				count+=1
			
	return count

def inList(alist, aValue):
	for i in alist:
		if aValue==i:
			return True
	return False
start_time = time.time()
print(circularPrimes(1000000))
print("--- %s seconds ---" % (time.time() - start_time))
