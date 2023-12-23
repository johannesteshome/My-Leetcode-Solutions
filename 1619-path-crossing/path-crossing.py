class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        # visited.add((0,0))

        def func(coord, i):
            # print(coord)
            if coord in visited:
                return True

            if i == len(path):
                return

            
            visited.add(coord)

            if path[i] == "N":
                res = func((coord[0], coord[1] + 1), i+1)
            if path[i] == "S":
                res = func((coord[0], coord[1] - 1), i+1)
            if path[i] == "E":
                res = func((coord[0] - 1, coord[1]), i+1)
            if path[i] == "W":
                res = func((coord[0] + 1, coord[1]), i+1)
            
            if res:
                return True

        return func((0,0), 0)