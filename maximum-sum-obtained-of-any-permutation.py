class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefixSum = [0 for r in range(len(nums)+1)]
        # print(prefixSum)
        for request in requests:
            prefixSum[request[0]] += 1
            prefixSum[request[1] + 1] -= 1
        # print(prefixSum)
        for i in range(len(prefixSum)-1):
            prefixSum[i+1] += prefixSum[i]
        # print(prefixSum)
        prefixSum.sort(reverse=True)
        nums.sort(reverse=True)
        # print(nums)
        # print(prefixSum)
        Sum = 0
        for index, num in enumerate(nums):
            Sum += (num * prefixSum[index])
        return Sum % (10**9 + 7)