class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(i, arr):
            nonlocal answer
            if len(arr) == len(nums):
                answer.append(arr)
                return 
            
            for j in range(len(nums)):
                if nums[j] not in arr:
                    backtrack(j, arr+[nums[j]])
        backtrack(-1, [])
        return answer