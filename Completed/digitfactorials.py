#Time To Run: 0.551165103912 seconds
import math
import time
def testIfGood(maxBound):
	t_sum = 0
	for i in range(3, maxBound):
		number = list(str(i))
		#print number
		sum = 0
		for k in number:
			sum += math.factorial(int(k))
		#print sum
		if sum == i:
			t_sum+=sum
	return t_sum
start_time = time.time()
print testIfGood(100000)
print("--- %s seconds ---" % (time.time() - start_time))
