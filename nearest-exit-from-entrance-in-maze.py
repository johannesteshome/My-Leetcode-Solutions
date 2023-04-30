class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direction = [(1,0), (-1, 0), (0,1), (0,-1)]
        visited = set([(entrance[0], entrance[1])])
        queue = deque([(entrance[0], entrance[1])])
        m, n = len(maze), len(maze[0])
        level = 0
        found = False

        while queue:
            currLevel = len(queue)
            # print(visited, queue)

            for _ in range(currLevel):
                node = queue.popleft()
                # print(node)

                if node[1] == 0 or node[0] == 0 or node[0] == m-1 or node[1] == n-1:
                    if node != (entrance[0], entrance[1]):
                        # print("here")
                        found = True
                        break
                
                for dir in direction:
                    x = node[0] + dir[0]
                    y = node[1] + dir[1]

                    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
                        if maze[x][y] == "." and (x,y) not in visited:
                            queue.append((x,y))
                            visited.add((x,y))
                
            if found:
                return level
            level += 1

        return -1