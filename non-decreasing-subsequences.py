class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answers = []
        # print(nums)

        def backtrack(i, answer):
            nonlocal answers
            # print(answers)
            
            if i >= len(nums):
                return
            if len(answer) >= 1:
                if answer[-1] <= nums[i]:
                    answer.append(nums[i])
                    if answer not in answers:
                        answers.append(answer)
                else:
                    return
            else:
                answer.append(nums[i])
            
            for j in range(i+1, len(nums)):
                backtrack(j, answer.copy())
        
        for i in range(len(nums)):
            backtrack(i, [])
        return answers