class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # totalSum = sum(nums)
        prefixSum = [0]
        hashmap = defaultdict(int)
        hashmap[0] = 1
        ans = 0


        for i in range(len(nums)):
            
            prefixSum.append(prefixSum[i] + nums[i])
            # print(i, prefixSum[i + 1] - k, hashmap)

            if (prefixSum[i + 1] - k) in hashmap:
                ans += hashmap[prefixSum[i + 1] - k]

            hashmap[prefixSum[i + 1]] += 1 
        
        return ans