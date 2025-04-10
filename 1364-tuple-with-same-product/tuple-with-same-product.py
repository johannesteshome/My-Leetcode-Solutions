class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                hashmap[nums[i] * nums[j]].append((nums[i], nums[j]))

        for key in hashmap:
            if len(hashmap[key]) > 1:
                total_comb = math.comb(len(hashmap[key]), 2)
                ans += total_comb * 8
        
        return ans