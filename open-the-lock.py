class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        increments = [1, -1]
        queue = deque(["0000"])
        visited = set()
        path = 0

        while queue:
            length = len(queue)

            for _ in range(length):
                lock = queue.popleft()

                if lock == target:
                    print(len(visited))
                    return path
                

                for i in range(len(lock)):
                    for inc in increments:
                        if lock[i] == "0" and inc == -1:
                            newLock = lock[:i] + "9" + lock[i+1:]
                        elif lock[i] == "9" and inc == 1:
                            newLock = lock[:i] + "0" + lock[i+1:]
                        else:
                            newLock = lock[:i] + str(int(lock[i]) + inc) + lock[i+1:]
                    
                        if newLock in deadends or newLock in visited:
                            continue
                    
                        visited.add(newLock)
                        queue.append(newLock)
            path += 1
        
        
        return -1