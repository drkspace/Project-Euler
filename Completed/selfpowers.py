#Time To Run: 4.41531896591 seconds
import math
import time
def selfpower(under):
	under += 1
	sum = 0
	for i in range(1, under):
		sum += power(i,i)
		#sum = list(str(sum))
		#del sum[len(sum)-1]
		#del sum[len(sum)-1]
		#sum = int(''.join(sum))
		while(len(str(sum))>10):
			sum = list(str(sum))
			del sum[0]
			sum = int(''.join(sum))
	return sum
def power(x,e):
	tot = 1
	for i in range(0,e):
		tot*=x
		while(len(str(tot))>10):
			tot = list(str(tot))
			del tot[0]
			tot = int(''.join(tot))
	return tot
start_time = time.time()	
print selfpower(1000)
print("--- %s seconds ---" % (time.time() - start_time))
