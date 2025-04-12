class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        memo = set()
    
        def backtrack(startIndex):
            if startIndex == len(s):
                return True
            
            memo.add(startIndex)
            
            for j in range(startIndex, len(s)):
                if s[startIndex:j+1] in wordDictSet and j+1 not in memo:
                    if backtrack(j+1):
                        return True
                
            
            return False
    
        return backtrack(0)