class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = []
        self.tracker = -1
        self.counter = defaultdict(int)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.counter[num] += 1
        
        while len(self.queue) > self.k:
            rear = self.queue.pop(0)
            self.counter[rear] -= 1
            if self.counter[rear] == 0:
                del self.counter[rear]
        
        return self.counter[num] == self.k
        
        # if num == self.value:
        #     self.tracker -= 1
        #     if len(self.queue) < self.k:
        #         # print(self.tracker, self.queue, "1st")
        #         self.queue.append(num)
        #         if len(self.queue) == self.k and self.tracker <= -1:
        #             return True
        #         return False
        #     else:
        #         # print(self.tracker, self.queue, "2nd")
        #         self.queue.pop(0)
        #         self.queue.append(num)
        #         if self.tracker <= -1: return True
        #         elif self.tracker > -1: return False 
        #         return True
        # else:
        #     if len(self.queue) < self.k:
        #         # print(self.tracker, self.queue, "3rd")
        #         self.queue.append(num)
        #         self.tracker = len(self.queue)-1
        #         return False
        #     else:
        #         # print(self.tracker, self.queue, "4th")
        #         self.queue.pop(0)
        #         self.queue.append(num)
        #         self.tracker = len(self.queue)-1 
        #         return False
        
        # if len(self.queue) < self.k:
        #     self.queue.append(num)
        #     # print(self.queue, "1st", self.k, len(self.queue))
        #     if(len(self.queue) == self.k):
        #         if self.queue[0] == self.value and self.queue.count(self.queue[0]) == len(self.queue):
        #             return True
        #         else:
        #             return False
        #     # return False
        # else:
        #     self.queue.pop(0)
        #     self.queue.append(num)
        #     # print(self.queue, "2nd")
        #     if self.queue[0] == self.value and self.queue.count(self.queue[0]) == len(self.queue):
        #         return True
        #     else:
        #         return False
            
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)