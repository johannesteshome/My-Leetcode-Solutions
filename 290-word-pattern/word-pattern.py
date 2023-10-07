class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = defaultdict(set)
        dic2 = defaultdict(set)
        sarr = s.split(" ")
        # print(sarr)
        # print(len(pattern))
        if len(pattern) != len(sarr):
            return False
        
        for i in range(len(pattern)):
            dic[pattern[i]].add(sarr[i])
            dic2[sarr[i]].add(pattern[i])
        
        # print(dic)
        
        for key in dic:
            if len(dic[key]) > 1:
                return False
        
        # print(dic2)
        for key in dic2:
            if len(dic2[key]) > 1:
                return False
        
        return True