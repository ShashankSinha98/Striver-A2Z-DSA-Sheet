class StockSpanner:

    def __init__(self):
        self.st = []
        self.i = 0

    def next(self, price: int) -> int:
        if len(self.st) == 0:
            self.st.append((price, self.i))
            ans = self.i + 1
            self.i += 1
            return ans

        elif self.st[-1][0] > price:
            ans = self.i - self.st[-1][1]
            self.st.append((price, self.i))
            self.i+=1
            return ans
        
        else:
            self.st.pop()
            return self.next(price)


if __name__ == "__main__":
    s = StockSpanner()
    print(s.next(100))
    print(s.next(80))
    print(s.next(60))
    print(s.next(70))
    print(s.next(60))
    print(s.next(75))
    print(s.next(85))
    print(s.st)