class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missSoFar = arr[0] - 1

        if missSoFar >= k:
            if k < arr[0]:
                return k
            else:
                return k + 1

        for i in range(len(arr)-1):
            miss = arr[i+1] - arr[i] - 1

            if miss + missSoFar >= k:
                return arr[i] + (k - missSoFar)
            
            missSoFar += miss
        
        return arr[-1] + (k - missSoFar)

        