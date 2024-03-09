class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)

        Max = max(count.values())
        print(Max, count)
        ans = 0

        for key in count:
            if count[key] == Max:
                ans += 1
        
        return ans * Max