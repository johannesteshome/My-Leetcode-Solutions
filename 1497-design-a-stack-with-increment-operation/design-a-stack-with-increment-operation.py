class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = 0
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if self.size < self.capacity:
            self.stack.append(x)
            self.size += 1


    def pop(self) -> int:
        if self.size > 0:
            self.size -= 1
            val = self.stack.pop()
            return val
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.size < k:
            for i in range(self.size):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)