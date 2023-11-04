class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        Max = float("-inf")

        for l in left:
            Max = max(Max, l)
        
        for r in right:
            Max = max(Max, n-r)
        
        return Max