class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        zippedStrs = list(zip(*strs))
        count = 0
        
        for strss in zippedStrs:
            string = list(strss)
            sortedStr = sorted(string)
            # print(string, sortedStr)
            if string != sortedStr:
                count += 1
        
        return count
