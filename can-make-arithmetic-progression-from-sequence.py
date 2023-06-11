class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        ans = set()

        for i in range(len(arr) - 1):
            ans.add(arr[i+1] - arr[i])
        
        return len(ans) == 1