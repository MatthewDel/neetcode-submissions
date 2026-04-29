class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        count = 0
        index = len(self.stack) - 1
        while index >= 0 and price >= self.stack[index]:
            index -= 1
            count += 1
        
        return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Number of consecutive days going backward such that those day prices are <=
# current day