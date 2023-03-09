class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(idx, arr):
            if sum(arr) == target:
                arr = sorted(arr)
                if arr not in ans:
                    ans.append(arr)
                return
            
            if sum(arr) > target:
                return

            for i in range(len(candidates)):
                backtrack(i, arr+[candidates[i]])
        
        backtrack(0, [])
        return ans