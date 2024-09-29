from typing import Optional

class MaxHeap:
    def __init__(self, maxHeapSize: int) -> None:
        self.heapArr = [None] * maxHeapSize
        self.lastElementIdx = -1
        self.maxHeapSize = maxHeapSize

    def size(self) -> int:
        return self.lastElementIdx + 1
    
    def insert(self, element: int):
        if self.lastElementIdx+1 == self.maxHeapSize:
            raise Exception("Cannot insert more elements, heap size full")
        
        # insert element at last
        self.lastElementIdx += 1
        self.heapArr[self.lastElementIdx] = element
        currPos: int = self.lastElementIdx

        while(currPos > 0):
            parentIdx: int = (currPos-1)//2

            if self.heapArr[parentIdx] < self.heapArr[currPos]:
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
            largestElementIdx = currPos

            if self.getLeftChild(currPos) != None and self.getLeftChild(currPos) > self.heapArr[currPos]:
                largestElementIdx = 2*currPos + 1
            
            if self.getRightChild(currPos) != None and self.getRightChild(currPos) > self.heapArr[largestElementIdx]:
                largestElementIdx = 2*currPos + 2
            
            if largestElementIdx==currPos:
                break
            
            self.heapArr[currPos], self.heapArr[largestElementIdx] = self.heapArr[largestElementIdx], self.heapArr[currPos]
            currPos = largestElementIdx

        return res
    
    def getLeftChild(self, idx: int) -> Optional[int|None]:
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
    mh = MaxHeap(maxHeapSize=10)
    for i in range(1, 11):
        mh.insert(i)
    mh.printArr()

    while(mh.size()>0):
        popedElem = mh.pop()
        print(f"Pop: {popedElem}")
    
    mh.printArr()
