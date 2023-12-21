class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        Max = float("-inf")
        
        for i in range(len(points) - 1):
            pointA = points[i]
            pointB = points[i+1]

            Max = max(Max, abs(pointB[0] - pointA[0]))
        
        return Max