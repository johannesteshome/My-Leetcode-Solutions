class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        for i in range(len(times)):
            times[i].append(i)

        times.sort()  
        # print(times)

        curr = 0
        occupied = []
        available = []
        chair = 0

        for i in range(len(times)):
            # print(i)
            # print(occupied)
            # print(available)
            if not occupied:
                available = []
                curr = 0
                chair = 0
                heappush(occupied, (times[i][1], curr))
                curr += 1
            else:
                while occupied and occupied[0][0] <= times[i][0]:
                    lastChair = heappop(occupied)
                    heappush(available, lastChair[1])
                if not occupied:
                    available = []
                    curr = 0
                    chair = 0
                    heappush(occupied, (times[i][1], curr))
                    curr += 1
                else:
                    if not available:
                        chair = curr
                        heappush(occupied, (times[i][1], curr))
                        curr += 1
                    else:
                        chair = heappop(available)
                        heappush(occupied, (times[i][1], chair))
            
            if times[i][2] == targetFriend:
                return chair


                
                    

