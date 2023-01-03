class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        totalSum = 0
        for num in nums:
            if(num % 2 == 0):
                totalSum += num
            
        for query in queries:
            if(nums[query[1]]%2 == 0):
                totalSum -= nums[query[1]]
            nums[query[1]] += query[0]
            if((nums[query[1]]) % 2 == 0):
                    totalSum += nums[query[1]]
            answer.append(totalSum)
            
        return answer