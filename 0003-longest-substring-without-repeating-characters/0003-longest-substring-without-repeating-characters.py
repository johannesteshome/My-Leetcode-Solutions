class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        Max = 0
        count = 0
        chars = []
        while(right < len(s)):
            if(s[right] in chars):
                chars = []
                left += 1
                right = left
                Max = max(count, Max)
                count = 0
            else:
                chars.append(s[right])
                count+=1
                Max = max(count, Max)
                right += 1
                
        return Max
        