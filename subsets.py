class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(idx, arr):
            ans.append(arr[:])
            # if len(ans) == 2**len(nums):
            #     return

            for i in range(idx, len(nums)):
                backtrack(i+1, arr+[nums[i]])
        
        backtrack(0, [])
        return ans