class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counted = Counter(nums)
        for num in counted:
            if counted[num] == 1:
                return num