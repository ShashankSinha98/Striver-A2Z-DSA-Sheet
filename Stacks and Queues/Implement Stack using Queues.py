class MyStack:

    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []
        

    def push(self, x: int) -> None:
        while len(self.queue_1) != 0:
            item = self.queue_1.pop(0)
            self.queue_2.append(item)
        
        self.queue_1.append(x)
        while len(self.queue_2) != 0:
            item = self.queue_2.pop(0)
            self.queue_1.append(item)

    def pop(self) -> int:
        if len(self.queue_1) == 0:
            return -1
        
        item = self.queue_1.pop(0)
        return item

    def top(self) -> int:
        if len(self.queue_1) == 0:
            return -1
        
        item = self.queue_1[0]
        return item

    def empty(self) -> bool:
        return len(self.queue_1) == 0