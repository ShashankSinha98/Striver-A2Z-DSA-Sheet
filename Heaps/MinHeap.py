from typing import Optional

class MinHeap:
    def __init__(self, minHeapSize: int) -> None:
        self.heapArr = [None] * minHeapSize
        self.lastElementIdx = -1
        self.minHeapSize = minHeapSize

    def size(self) -> int:
        return self.lastElementIdx + 1
    
    def insert(self, element: int):
        if self.lastElementIdx+1 == self.minHeapSize:
            raise Exception("Cannot insert more elements, heap size full")
        
        # insert element at last
        self.lastElementIdx += 1
        self.heapArr[self.lastElementIdx] = element
        currPos: int = self.lastElementIdx

        while(currPos > 0):
            parentIdx: int = (currPos-1)//2

            if self.heapArr[parentIdx] > self.heapArr[currPos]:
                self.heapArr[parentIdx], self.heapArr[currPos] = self.heapArr[currPos], self.heapArr[parentIdx]
                currPos = parentIdx
            else:
                break

    def pop(self) -> Optional[int|None]:
        if self.size == 0:
            return None
        
        # Replace root with last element
        res = self.heapArr[0]
        self.heapArr[0] = self.heapArr[self.lastElementIdx]
        self.heapArr[self.lastElementIdx] = None # Optional step
        self.lastElementIdx -= 1

        currPos: int = 0
        # Move new root element at correct position
        while(not self.isLeaf(currPos)):
            smallestElementIdx = currPos

            if self.getLeftChild(currPos) != None and self.getLeftChild(currPos) < self.heapArr[currPos]:
                smallestElementIdx = 2*currPos + 1
            
            if self.getRightChild(currPos) != None and self.getRightChild(currPos) < self.heapArr[smallestElementIdx]:
                smallestElementIdx = 2*currPos + 2
            
            if smallestElementIdx==currPos:
                break
            
            self.heapArr[currPos], self.heapArr[smallestElementIdx] = self.heapArr[smallestElementIdx], self.heapArr[currPos]
            currPos = smallestElementIdx

        return res
    
    def getLeftChild(self, idx: int) -> Optional[int| None]:
        if (2*idx+1 <= self.lastElementIdx):
            return self.heapArr[2*idx+1]
        else:
            return None
        
    def getRightChild(self, idx: int) -> Optional[int| None]:
        if (2*idx+2 <= self.lastElementIdx):
            return self.heapArr[2*idx+2]
        else:
            return None

    def isLeaf(self, idx: int) -> bool:
        return (2*idx > self.lastElementIdx-1)
    
    def printArr(self):
        print(self.heapArr)


if __name__ == "__main__":
    mh = MinHeap(minHeapSize=10)
    for i in range(11, 1, -1):
        mh.insert(i)
    print(mh.printArr())

    while(mh.size()>0):
        print(f"pop: {mh.pop()}")
    
    mh.printArr()