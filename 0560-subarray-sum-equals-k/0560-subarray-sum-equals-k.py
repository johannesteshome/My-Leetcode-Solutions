class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Sum = 0;
        count = 0;
        
        Map = defaultdict(int)
        Map[0] = 1
        
        for i in range(len(nums)):
            Sum += nums[i]
            
            if Sum-k in Map:
                count += Map[Sum-k]
                
            Map[Sum] += 1
            
        return count