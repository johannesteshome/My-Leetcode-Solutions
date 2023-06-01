class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def ways(i, Sum):

            state = (i, Sum)

            if state in memo:
                return memo[state]

            if i == len(nums):
                if Sum == target:
                    return 1
                else: return 0
            
            memo[state] = ways(i+1, Sum + nums[i]) + ways(i+1, Sum - nums[i])
            return memo[state]
        
        return ways(0,0)