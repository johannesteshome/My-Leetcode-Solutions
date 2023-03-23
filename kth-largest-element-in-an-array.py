class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            print(left, right)
            # print(nums[left], nums[right], "the items")
            if right - left <= 0:
                if left == len(nums) - k:
                    return nums[left]
                return 
            
            pivot = right
            leftMost = left
            while left < right:
                if nums[left] < nums[pivot]:
                    left += 1
                else:
                    if nums[right] >= nums[pivot]:
                        right -= 1
                    else:
                        nums[left], nums[right] = nums[right], nums[left]
            
            nums[left], nums[pivot] = nums[pivot], nums[left]

            if left == len(nums) - k:
                return nums[left]
            
            leftHalf = partition(leftMost, left-1)
            rightHalf = partition(left+1, pivot)

            if leftHalf != None:
                return leftHalf
            return rightHalf
            # return leftHalf or rightHalf
        
        return partition(0, len(nums) - 1)