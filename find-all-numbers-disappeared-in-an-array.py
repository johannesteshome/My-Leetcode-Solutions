class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        Map = defaultdict(list)
        while i < n:
            correct_position = nums[i] -1
            if correct_position != i:
                if nums[correct_position] == nums[i]:
                    Map[nums[i]] = i+1
                    i+=1
                else:
                    nums[correct_position], nums[i] = nums[i], nums[correct_position]
            else:
                i += 1
        return Map.values()