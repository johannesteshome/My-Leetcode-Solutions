class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        zippedStr = list(zip(*strs))
        for strs in zippedStr:
            for i in range(0, len(strs) - 1):
                if(ord(strs[i]) > ord(strs[i+1])):
                    count += 1
                    break
                    
        return count