class Solution:
    def similarPairs(self, words: List[str]) -> int:
        left = 0
        right = 1
        count = 0
        
        while(left <= len(words) - 2):
            leftStr = set(words[left])
            while(right <= len(words) - 1):
                similar = True
                rightStr = set(words[right])
                if(leftStr == rightStr):
                    count += 1
                right += 1
            left += 1
            right = left + 1
        
        return count
                    
                        