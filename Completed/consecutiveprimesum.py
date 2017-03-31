#Time To Run: 
import math
import time
def generatePrimes(under):
	primes = [2]
	i = 3
	while(i<under):
		root = math.sqrt(i)
		#print(i)
		for k in primes:
			if(i%k==0):
				break
			if(k>root):
				#print("Should add")
				primes.append(i)
				break
		#print(i)
		i+=2
	#print len(primes)
	print("Done Generating primes")
	return primes
def longChainFinder(under):
	longChain = 0
	highest = 0
	primes = generatePrimes(under)
	for i in range(0,len(primes)):
		chain = 0
		k = 0
		sum = 0
		while(sum<1000000):
			if((i+k)>=len(primes)):
				break
			sum+=primes[i+k]
			if sum in primes:
				if k > longChain:
					longChain = k
					highest = sum
			k+=1
	return highest
start_time = time.time()
print longChainFinder(1000000)
print("--- %s seconds ---" % (time.time() - start_time))
