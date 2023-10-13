class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        x1 = coordinates[1][0]
        y1 = coordinates[1][1]
        dx = x1 - x0
        dy = y1 - y0
        for i in range(len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            if (dx * (y - y1) != dy * (x - x1)):
                # print("NO")
                return False
        # print("YES")
        return True