class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            Min = min(abs(x2 - x1), abs(y2 - y1))
            Max = max(abs(x2 - x1), abs(y2 - y1))
            ans = ans + Min + (Max - Min)
        
        return ans
