class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)):
            if target == nums[i]:
                ans.append(i)
                
        return ans