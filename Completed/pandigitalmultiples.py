#Time to run: 0.115843057632 seconds 
import math
import time
def isPandigital(num):
	num = list(str(num))
	for i in num:
		if num.count(i)>1:
			return False
	for i in range(1,len(num)+1):
		if num.count(str(i))!=1:
			return False
	return True
def multiples():
	for i in xrange(99999,1,-1):
		num = ""
		k=0	
		while True:
			k+=1
			num=num+str(k*i)
			if len(num)<9:
				continue
			if len(num)>9:
				break
			if len(num)==9:
				if isPandigital(int(num)):
					return num
start_time = time.time()
print multiples()		
print("#Time to run: %s seconds " % (time.time() - start_time))
