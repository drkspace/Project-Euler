def answer(data, n):
    for p in range(0,len(data)):
       for i in range(0,len(data)):
            correctIndex=[i]
            counter = 1
            for k in range(i+1,len(data)):
                if(data[k]==data[i]):
                   counter+=1
                   correctIndex.append(k)
            if(counter>n):
                try:
                  for j in xrange(len(correctIndex)-1,-1,-1):
                        del data[correctIndex[j]]
                except IndexError:
                   break
    return data
    
a = [1,2,2,2,3,3,1]
print answer(a,1)
