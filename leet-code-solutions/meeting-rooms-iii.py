class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = []
        free = []
        count = defaultdict(int)

        for i in range(n):
            free.append(i)

        meetings.sort()
            
        heapify(rooms)
        heapify(free)

        Max = float("-inf")
        print(meetings)

        for meeting in meetings:

            # print(rooms, free)
            while rooms and rooms[0][0] <= meeting[0]:
                heappush(free, heappop(rooms)[1])
            
            if free:
                room = heappop(free)
                heappush(rooms, (meeting[0] + (meeting[1] - meeting[0]), room))
                count[room] += 1
            else:
                # print("here", meeting, meeting[1] - meeting[0])
                time, room = heappop(rooms)
                time += (meeting[1] - meeting[0])
                count[room] += 1

                heappush(rooms, (time, room))

        
        ans = -1
        # print(count)
        for k in count:
            if count[k] > Max:
                ans = k
                Max = count[k]
        
        return ans