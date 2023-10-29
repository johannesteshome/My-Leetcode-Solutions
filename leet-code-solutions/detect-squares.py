class DetectSquares:

    def __init__(self):
        self.hashmap = defaultdict(int)
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.hashmap[(point[0], point[1])] += 1
        self.points.append((point[0], point[1]))
        

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point
        
        for x, y in self.points:
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            count += (self.hashmap[(x, py)] * self.hashmap[(px, y)])
            
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)