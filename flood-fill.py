class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        original = image[sr][sc]
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()

        def flood(x, y):
            # print(x,y)
            if not (0 <= x < m) or not (0 <= y < n):
                return 
            if image[x][y] != original or (x,y) in visited:
                visited.add((x,y))
                return
            else:
                visited.add((x,y))
                image[x][y] = color
            for dir in direction:
                flood(x+dir[0], y+dir[1])

        flood(sr, sc)

        return image