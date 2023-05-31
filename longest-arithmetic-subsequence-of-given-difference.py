class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}

        memo[arr[0]] = 1
        Max = 1

        for i in range(1, len(arr)):
            if arr[i] - difference in memo:
                memo[arr[i]] = 1 + memo[arr[i] - difference]
                Max = max(memo[arr[i]], Max)
            else:
                memo[arr[i]] = 1

        return Max