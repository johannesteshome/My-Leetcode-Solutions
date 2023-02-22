class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = [0]
        
        for index, num in enumerate(self.nums):
            self.prefixSum.append(self.prefixSum[index] + num)

    def sumRange(self, left: int, right: int) -> int:
            
        return self.prefixSum[right+1] - self.prefixSum[left]
            
        # print(prefixSum)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)