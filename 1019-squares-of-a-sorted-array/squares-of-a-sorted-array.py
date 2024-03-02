class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return [nums[0] ** 2]
        
        ans = []
        if nums[0] >= 0:
            for i in range(len(nums)):
                ans.append(nums[i] ** 2)
            return ans
        
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] <= 0 and nums[right] > 0:
                break
            else:
                left += 1
                right += 1
        print(left, right, 'lr')
        while left >= 0 and right < len(nums):
            if nums[left] ** 2 < nums[right] ** 2:
                print('here', nums[left] ** 2)
                ans.append(nums[left] ** 2)
                left -= 1
            else:
                ans.append(nums[right] ** 2)
                right += 1
        
        if left >= 0:
            for i in range(left, -1, -1):
                ans.append(nums[i] ** 2)
        
        if right < len(nums):
            for i in range(right, len(nums)):
                ans.append(nums[i] ** 2)
        
        return ans
        