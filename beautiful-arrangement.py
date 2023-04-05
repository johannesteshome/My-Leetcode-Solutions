class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0

        def backtrack(arr, bit):
            # print(arr)
            nonlocal count
            if len(arr) == n:
                count += 1
                return
            
            for i in range(1, n+1):
                if bit & (1<<i) != 0:
                    continue
                if (len(arr)+1) % i == 0 or i % (len(arr)+1) == 0:
                    backtrack(arr+[i], bit | (1<<i))
                
            
        backtrack([], 0)
        return count