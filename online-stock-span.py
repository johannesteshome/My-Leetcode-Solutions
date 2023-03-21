class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price, 1])
            return self.stack[-1][1]
        if self.stack and self.stack[-1][0] > price:
            self.stack.append([price, 1])
            return self.stack[-1][1]
        elif self.stack and self.stack[-1][0] <= price:
            temp = [price, 1]
            while self.stack and self.stack[-1][0] <= price:
                temp[1] += self.stack.pop()[1]
            self.stack.append(temp)
            return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)