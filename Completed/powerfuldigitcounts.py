#Time To Run: 0.000273942947388 seconds
import math
import time
def powerCount(maxPower):	
	count = 0
	for i in range(1, maxPower+1):
		for k in range (1, 10):
			dig = math.log10(k)
			if(math.floor(i*dig+1) == i):
				count+=1
				continue
	return count
start_time = time.time()
print powerCount(25)
print("--- %s seconds ---" % (time.time() - start_time))
