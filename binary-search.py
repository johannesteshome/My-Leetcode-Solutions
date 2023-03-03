class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = (left + right + 1)//2

        while left <= right:
            if nums[mid] < target:
                left = mid+1
                mid = (left+right + 1)//2
            elif nums[mid] > target:
                right = mid - 1
                mid = (left+right + 1)//2
            else:
                return mid
        return -1