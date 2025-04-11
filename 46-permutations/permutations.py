class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(j, arr):
            nonlocal ans
            if len(arr) == len(nums):
                ans.append(arr)
                return

            for i in range(len(nums)):
                if i != j and nums[i] not in arr:
                    backtrack(i, arr + [nums[i]])
        
        backtrack(-1, [])

        return ans