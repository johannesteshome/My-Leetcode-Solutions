class Solution:
    def sumDivide(self, divisor, nums):
        Sum = 0
        for num in nums:
            Sum += math.ceil(num/divisor)
        return Sum

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            mid = (left+right) // 2
            # print(mid, left, right)
            Sum = self.sumDivide(mid, nums)
            
            # print(Sum)
            if Sum <= threshold:
                right = mid
            elif Sum > threshold:
                left = mid + 1
        return right
            
        # return 0