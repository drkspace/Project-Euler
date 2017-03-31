import math
import time
def findDivisors(num):
	div=[1]
	for i in range(2,int(math.ceil(math.sqrt(num)))+1):
		if num%i==0:
			div.append(i)
	div2=[]	
	for k in div:
		div2.append(num/k)
	div.extend(div2)
	return div
def findSqrSum(aList):
	sum = 0
	for i in aList:
		sum+=(i*i)
	return sum
def isSqr(num):
	if math.sqrt(num).is_integer():
		return True
	return False
def findSum(start, end):
	
	sum = 0
	i=start
	while(i<=end):
		start_time = time.time()
		i+=1
		#print i
		div = findDivisors(i)
		tot = findSqrSum(div)
		if isSqr(tot):
			#print i
			#print div
			sum+=i
		print("#Time to run: %s seconds " % (time.time() - start_time))	
	print sum
	
start_time = time.time()
print findDivisors(42)
#findSum(1,64000000)
print("#Time to run: %s seconds " % (time.time() - start_time))
