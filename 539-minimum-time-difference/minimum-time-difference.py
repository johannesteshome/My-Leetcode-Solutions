class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        ans = float("inf")

        for i in range(len(timePoints)):
            hour = int(timePoints[i][:2])
            minute = int(timePoints[i][3:])
            
            diff = hour * 60
            diff += minute

            minutes.append(diff)
            
        minutes.sort()

        ans = min(minutes[i+1] - minutes[i] for i in range(len(minutes) - 1))
        
        return min(ans, 24 * 60 - minutes[-1] + minutes[0])