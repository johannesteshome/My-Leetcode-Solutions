class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        # lists use append 
        answer.append(nums[0])
        
        for index in range(1, len(nums)):
            answer.append(nums[index] + answer[index-1])
            
        return answer