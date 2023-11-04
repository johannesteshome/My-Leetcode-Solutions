class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        arr = set()
        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                arr.add(1)
            elif nums[i+1] < nums[i]:
                arr.add(-1)
            else:
                arr.add(0)

        if len(arr) > 2:
            return False
        arr = list(arr)

        if len(arr) == 1:
            if arr[0] == 1 or arr[0] == -1 or arr[0] == 0:
                return True
        if len(arr) == 2:
            Max = max(arr)
            Min = min(arr)

            if Max == 0 and Min == -1:
                return True
            if Max == 1 and Min == 0:
                return True
            else:
                return False