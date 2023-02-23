class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        left = 0
        right = length - 1
        sDict = defaultdict(int)
        pDict = defaultdict(int)
        answer = []
        
        if length > len(s):
            return []
        
        for pp in p:
            pDict[pp] += 1
            
        for i in range(length):
            sDict[s[i]] += 1
            
        # print(sDict, pDict)
            
        if sDict == pDict:
            answer.append(left)
            
        right += 1
        left += 1
        
        while right < len(s):
            # print(sDict, right)
            if sDict[s[left-1]] == 1:
                sDict.pop(s[left-1])
            elif sDict[s[left - 1]] > 1:
                sDict[s[left - 1]] -= 1
            sDict[s[right]] += 1
            
            if sDict == pDict:
                answer.append(left)
            
            right += 1
            left += 1
        
        return answer