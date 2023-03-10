class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(j, arr):
            nonlocal answer
            if j > n:
                return

            if len(arr) == k:
                answer.append(arr)
                return
            
            for i in range(j+1, n+1):
                backtrack(i, arr+[i])
        
        backtrack(0, [])
        return answer