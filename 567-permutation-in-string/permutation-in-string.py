class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) == 1:
            if s1[0] in s2:
                return True
            else:
                return False
            
        if len(s1) > len(s2):
            return False
        
        left = 0 
        right = len(s1) - 1
        myStr = defaultdict(int)
        myStr2 = defaultdict(int)
        
        for s in s1:
            myStr[s] += 1
            
        # print(myStr)
        
        for index in range(right + 1):
            myStr2[s2[index]] += 1
            
        # print(myStr2)
                  
            
        while right < len(s2) - 1:
            if myStr == myStr2:
                return True    
            if myStr2[s2[left]] == 1:
                del myStr2[s2[left]]
            else:
                myStr2[s2[left]] -= 1
            
            left += 1
            right += 1
            
            myStr2[s2[right]] += 1
            
        if myStr == myStr2:
            return True 
        
        return False
        
                