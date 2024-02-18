class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heapify(events)
        newEvent = 0
        lastDay = 0
        count = 0
        attendedEvents = defaultdict(int)

        while events:
            event = heappop(events)
            # print(event)

            lastDay = max(event[1], lastDay)

            if event[1] - event[0] + 1 <= attendedEvents[(event[0], event[1])]:
                continue

            temp = max(newEvent + 1, event[0])

            if temp <= lastDay:
                attendedEvents[(event[0], event[1])] += 1
                newEvent = temp
                count += 1
        
        return count


             
        