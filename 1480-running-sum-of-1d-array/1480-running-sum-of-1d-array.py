class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        answer.append(nums[0])
        
        for i in range(1, len(nums)):
            answer.append(answer[i-1] + nums[i])
            
        return answer