class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float("inf")  
        min_index = -1  
        for i, (a, b) in enumerate(points):
          
            distance = abs(x - a) + abs(y - b)
          
            if (a == x or b == y) and distance < min_distance:
                min_distance = distance
                min_index = i
        return min_index