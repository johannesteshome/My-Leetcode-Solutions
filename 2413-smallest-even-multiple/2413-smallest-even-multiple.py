class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiplesOfTwo = []
        
        for i in range(n):
            multiplesOfTwo.append((i+1)*2)
            
        print(multiplesOfTwo)
            
        multiplesOfN = []
        index = 1
        iterate = True
        while(iterate):
            multiplesOfN.append(n * index)
            if(n*index == n*2): iterate = False
            index += 1
                
        print(multiplesOfN)
                
        twoSets = set(multiplesOfTwo)
        nSets = set(multiplesOfN)
       
        return min(list(twoSets.intersection(nSets)))
        
        
        
    
                