#Time to run: 0.195223093033 seconds 
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
def loop():
	products=[]
	for i in range(1,10000):
		for k in range(1,1000):
			product=i*k
			combined = int(str(i)+str(k)+str(product))
					
			if combined>1000000000:
				break
			if combined<123456789:
				continue
			if isPandigital(combined):
				
				if product not in products:
					#print combined
					products.append(product)
					
	return sum(products)
start_time = time.time()
print loop()	
print("#Time to run: %s seconds " % (time.time() - start_time))
