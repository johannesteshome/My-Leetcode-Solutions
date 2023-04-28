class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        length = len(rooms)

        visited.add(0)
        queue.append(0)
        # print(rooms[1])

        while queue:
            # print(queue)
            currentRoom = queue.popleft()
            # print(currentRoom)

            for index in rooms[currentRoom]:
                # print(rooms[index], index)
                if index not in visited:
                    queue.append(index)
                    visited.add(index)
                    length -= 1

        if length == 1:
            return True
        return False