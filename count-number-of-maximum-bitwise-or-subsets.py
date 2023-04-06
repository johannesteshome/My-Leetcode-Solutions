class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        bit = 0
        Max = 0
        count = 0
        for i in range(len(nums)):
            bit ^= (1<<i)
        # print(bit)

        for i in range(bit+1):
            res = 0
            for j in range(32):
                if i & (1<<j) != 0:
                    res |= nums[j]

            if res > Max:
                Max = res
                count = 1
            elif res == Max:
                count += 1
        
        return count


        # return bit