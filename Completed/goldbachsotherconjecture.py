#Time to Run: 0.953160047531 seconds 
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
def run(under):
	primes = generatePrimes(under)
	rge = range(1,int(math.ceil(math.sqrt(under))))
	for i in xrange(9,under,2):
		if i in primes:
			continue
		#print i
		toBreak = False
		toCont = False
		for k in primes:
			if k>=i:
				break
			for j in rge:
				toCheck = k+(2*j*j)
				#print toCheck
				if toCheck==i:
					#print i
					toBreak = True
					break
				if toCheck>i:
					toCont = True
					break
			if toBreak:
				break
			if toCont:
				continue
		if(toBreak and toCont)==False:		
			return i
start_time = time.time()
print run(6000)
print("--- %s seconds ---" % (time.time() - start_time))
