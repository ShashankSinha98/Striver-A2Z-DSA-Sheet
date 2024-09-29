class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        

    def push(self, x: int) -> None:
        while len(self.stack_1) != 0:
            item = self.stack_1.pop()
            self.stack_2.append(item)
        
        self.stack_1.append(x)
        while len(self.stack_2) != 0:
            item = self.stack_2.pop()
            self.stack_1.append(item)

    def pop(self) -> int:
        if len(self.stack_1) == 0:
            return -1
        
        item = self.stack_1.pop()
        return item        

    def peek(self) -> int:
        if len(self.stack_1) == 0:
            return -1
        
        item = self.stack_1[len(self.stack_1)-1]
        return item        

    def empty(self) -> bool:
        return len(self.stack_1) == 0        