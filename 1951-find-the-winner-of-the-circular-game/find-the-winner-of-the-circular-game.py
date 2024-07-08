class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i+1 for i in range(n)]
        i=0
        while len(arr) > 1:
            i=(i+k-1)%n
            arr.pop(i)
            n-=1            
            
            
        return arr[0]