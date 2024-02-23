class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        numSet = set()
        binary = ["0", "1"]

        for num in nums:
            numSet.add(num)

        def backtrack(i, s):
            if i == len(nums):
                if s not in numSet:
                    return s
                else:
                    return
            
            for b in binary:
                res = backtrack(i+1, s+b)
                if res:
                    return res
        
        return backtrack(0, "")
      
        