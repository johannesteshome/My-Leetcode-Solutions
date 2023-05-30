class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        halfSum = sum(nums) // 2

        def dp(i, Sum):
            state = (i, Sum)

            if state in memo:
                return memo[state]

            if Sum < 0:
                return False
            
            if Sum == 0:
                return True
            
            if i == len(nums):
                return False

            memo[state] = dp(i+1, Sum - nums[i]) or dp(i+1, Sum)
            return memo[state]
        
        return sum(nums) % 2 == 0 and dp(0, halfSum)