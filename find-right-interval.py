class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        Map = defaultdict(int)
        for index, interval in enumerate(intervals):
            Map[interval[0]] = index
        
        newIntervals = []
        for i in intervals:
            newIntervals.append(i[0])
        newIntervals.sort()
        print(newIntervals, Map)
        answer = [-1] * len(intervals)

        for interval in intervals:
            res = bisect_left(newIntervals, interval[1])
            if res >= len(intervals):
                continue
            answer[Map[interval[0]]] = Map[newIntervals[bisect_left(newIntervals, interval[1])]]

        # for index, interval in enumerate(intervals):
        #     start = 0
        #     finish = len(intervals)-1

        #     while start <= finish:
        #         mid = (start+finish)//2
        #         if interval[1] > newIntervals[mid][0]:
        #             print(interval[1], newIntervals[mid][0], "up")
        #             start = mid + 1
        #         elif interval[1] < newIntervals[mid][0]:
        #             print(interval[1], newIntervals[mid][0], "down")
        #             finish = mid-1
        #         else:
        #             print(interval[1], newIntervals[mid][0], "found it")
        #             # print(Map[(interval[0], interval[1])], interval[0], interval[1])
        #             answer[Map[(interval[0], interval[1])]] = Map[(newIntervals[mid][0], newIntervals[mid][1])]
        #             break
        return answer