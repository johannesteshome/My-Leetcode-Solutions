class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda x : sqrt(x[0]**2 + x[1]**2))
        return points[:k]
        
    # def getDistanceFromZero(self, point: List[int]):
    #     return sqrt(point[0]**2 + point[1]**2)