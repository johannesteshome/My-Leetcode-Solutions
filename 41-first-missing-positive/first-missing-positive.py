class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = []

        for num in nums:
            if num > 0:
                bisect.insort(res, num)
        
        num = 0

        for n in res:
            if n > num + 1:
                return num + 1
            if n == num + 1:
                num += 1
        
        return num + 1