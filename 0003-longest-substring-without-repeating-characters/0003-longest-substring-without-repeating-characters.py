class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        right = 0
        Max = 0
        
        while right < len(s):
            if right == s.find(s[right], left):
                Max = max(Max, right-left+1)
                right += 1
            else:
                left += 1
                
            
        return Max
            