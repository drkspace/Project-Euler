#Time to run: 4.23408484459 seconds
import math
import time
def prime(num):
	if num%2==0 and num!=2:
		return False
	if num==1:
		return False
	for i in xrange(3,int(math.ceil(math.sqrt(num)))+1,2):
		if num%i==0:
			return False
	return True
def truncate(num):
	tmp = num
	tmp = str(tmp)
	while(len(tmp)>0):
		if prime(int(tmp))==False:
			return False
		tmp = list(tmp)
		del tmp[0]
		tmp = ''.join(tmp)
	tmp = num
	tmp = str(tmp)
	while(len(tmp)>0):
		if prime(int(tmp))==False:
			return False	
		tmp = list(tmp)
		del tmp[len(tmp)-1]
		tmp = ''.join(tmp)
	return True
def testIfWorks():
	sum = 0
	hits = 0
	i = 9
	while(hits!=11):
		i+=2
		if truncate(i):
			#print i
			sum+=i
			hits+=1
			if(hits==11):
				return sum
	return "FAIL"
start_time = time.time()
print testIfWorks()
print("--- %s seconds ---" % (time.time() - start_time))	
