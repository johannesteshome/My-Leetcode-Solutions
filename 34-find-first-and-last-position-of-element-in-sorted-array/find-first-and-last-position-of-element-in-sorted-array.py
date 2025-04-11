class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        ans = []

        ans.append(bisect_left(nums, target))
        ans.append(bisect_right(nums, target))

        if ans[0] == ans[1]:
            return [-1, -1]
        return [ans[0], ans[1] - 1]

        return ans


        # low = 0
        # high = len(nums) - 1

        # while low <= high:

        #     mid = (low + high) // 2


        