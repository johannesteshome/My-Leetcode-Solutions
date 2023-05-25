class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        Min = nums[0]
        subsequence = []
        
        for num in nums[1:]:
            if num <= Min:
                Min = num
            else:
                subsequence.append(num)
        
        print(subsequence)
        if not subsequence:
            return False
        Min = subsequence[0]
        for sub in subsequence[1:]:
            if sub <= Min:
                Min = sub
            else:
                return True

        
        return False