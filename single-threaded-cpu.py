class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        currTasks = []
        answer = []

        for index, task in enumerate(tasks):
            task.append(index)

        heapify(tasks)
        # print(tasks)

        task = heappop(tasks)
        time = task[0]
        currTime = time + task[1]
        answer.append(task[2])

        while tasks:
            while tasks and tasks[0][0] <= currTime:
                start, duration, index = heappop(tasks)
                heappush(currTasks, [duration, index, start])
            if not currTasks:
                start, duration, index = heappop(tasks)
                currTime = currTime + duration + start
                answer.append(index)
            else:
                duration, index, start = heappop(currTasks)
                currTime += duration
                answer.append(index)
        
        while currTasks:
            duration, index, start = heappop(currTasks)
            answer.append(index)

        return answer