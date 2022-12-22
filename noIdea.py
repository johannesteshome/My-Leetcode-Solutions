# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

size = [int(i) for i in input().split(' ')]
arrayList = [int(i) for i in input().split(' ')]
setA = [int(i) for i in input().split(' ')]
setB = [int(i) for i in input().split(' ')]
arrayMap ={}
happiness = 0

        
arrayMap = collections.Counter(arrayList)
         

for i in range(size[1]):
        happiness = happiness + arrayMap.get(setA[i], 0)
        happiness = happiness - arrayMap.get(setB[i], 0)

    
print(happiness)
    
