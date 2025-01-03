class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        answer = 0

        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[i-1] + nums[i])
        
        for i in range(1, len(prefixSum)):
            if prefixSum[i-1] >= (prefixSum[-1] - prefixSum[i-1]):
                answer += 1
        
        return answer