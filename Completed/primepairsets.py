#Time To Run: 3.97849392891 seconds
import math
import time
primes = []
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

def findSequence(under):
	global primes
	primes = generatePrimes(under)
	#print primes
	#max_length = len(str(primes[len(primes)-1]))
	#print max_length
	#sums = []
	for i in primes:
		if i == 5:
			continue
		if i == 2:
			continue
		if i>100:
			break
		#works = isPrime(primes, i)
		#if len(works)==0:
		#	continue
		#print works
		#print i
		for k in range(1,len(primes)):
			good = [i]
			if concatPrime(i, primes[k])==False:
				continue
			good.append(primes[k])
			for j in range(k+1,len(primes)):
				for l in good:
					toCont = False
					#print good
					if concatPrime(l, primes[j])==False:
						toCont = True
						break	
				if toCont:
					continue
				good.append(primes[j])
							
			if len(good)==5:
				#print good
				return sum(good)
				sums.append(sum(good))
				#break
			del good[:]
	low = 0
	for k in sums:
		if k < low:
			low = k
	
	return(k)
def isPrime(aList, num):
	works=[]
	for i in aList:
		if concatPrime(num, i):
			works.append(i)
	
	return works
def concatPrime(num1, num2):
	num = str(num1)+str(num2)
	num = int(num)
	if prime(num):
		num = str(num2)+str(num1)
		num = int(num)
		if prime(num):
			return True
		else:
			return False
	else:
		return False
def prime(num):
	if num%2==0:
		return False
	for i in xrange(3,int(math.ceil(math.sqrt(num))),2):
		if num%i==0:
			return False
	return True
start_time = time.time()
print findSequence(10000)
print("--- %s seconds ---" % (time.time() - start_time))
#print generatePrimes(100)
#print concatPrime(3,7)

