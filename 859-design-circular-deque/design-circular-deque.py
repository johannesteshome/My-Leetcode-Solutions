class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0 for _ in range(k)]
        self.front = 0
        self.rear = k-1
        self.k = k
        self.size = 0
        

    def insertFront(self, value: int) -> bool:
        # print(self.deque, value, 'insertFront')
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k
        self.deque[self.front] = value
        self.size += 1
        return True        

    def insertLast(self, value: int) -> bool:
        # print(self.deque, value, 'insertLast')

        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k
        self.deque[self.rear] = value
        self.size += 1
        return True
        
    def deleteFront(self) -> bool:
        # print(self.deque, 'deleteFront')

        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        # print(self.deque, 'deleteLast')

        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        # print(self.deque, 'getFront')

        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        # print(self.deque, 'getRear')

        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        # print(self.deque, 'isEmpty')

        return self.size == 0

    def isFull(self) -> bool:
        # print(self.deque, 'isFull')

        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()