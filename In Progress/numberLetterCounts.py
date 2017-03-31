import sys
sys.path.insert(0,"/home/daniel/pythonstuff/KramerResources")
from Kramer_math import numberLetterCount as nlc
sum=0
for i in xrange(1,1000+1):
	sum+=nlc(i)
print sum
