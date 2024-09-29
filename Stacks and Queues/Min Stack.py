import sys


class MinStack:

    def __init__(self):
        self.st = []
        self.min = sys.maxsize
        

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.st.append(val)
            self.min = val
        
        elif val < self.min:
            self.st.append(2*val - self.min)
            self.min = val
        
        else:
            self.st.append(val)


    def pop(self) -> None:
        n = len(self.st)
        if n == 0:
            return
        
        if self.st[n-1] < self.min:
            act_val = self.min
            self.min = 2*self.min - self.st[n-1]
            self.st.pop()
            return act_val
        else:
            val = self.st[n-1]
            self.st.pop()
            return val

    def top(self) -> int:
        n = len(self.st)

        if self.st[n-1] < self.min:
            return self.min
        else:
            return self.st[n-1]        

    def getMin(self) -> int:
        return self.min
        

if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    ms.pop()
    print(ms.getMin())
