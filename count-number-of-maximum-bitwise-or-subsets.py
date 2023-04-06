class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        Max = 0
        count = 0

        def backtrack(arr, i):
            # print(arr)
            nonlocal Max
            nonlocal count
            # print(count)

            res = 0
            for k in range(len(arr)):
                res |= arr[k]
            
            if res > Max:
                Max = res
                count = 1
            elif res == Max:
                count += 1
            
            if len(arr) == len(nums):
                return

            for j in range(i+1, len(nums)):
                backtrack(arr+[nums[j]], j)
        
        backtrack([], -1)

        return count