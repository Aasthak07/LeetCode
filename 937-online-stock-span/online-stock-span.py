class StockSpanner:

    def __init__(self):
        self.st = []  # (price, count)

    def next(self, price: int) -> int:
        count = 1

        # Same logic as NGE: remove smaller elements
        while self.st and self.st[-1][0] <= price:
            count += self.st[-1][1]
            self.st.pop()

        self.st.append((price, count))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)