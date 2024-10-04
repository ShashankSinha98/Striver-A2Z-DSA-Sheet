import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        # adding to max heap by default
        heapq.heappush(self.maxHeap, -1*num)

        # checking if maxheap top <= minheap top
        if len(self.minHeap)>0 and not (-1)*self.maxHeap[0] <= self.minHeap[0]:
            tmp = -1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, tmp)

        # balancing length
        if len(self.maxHeap)-len(self.minHeap)>1:
            tmp = -1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, tmp)
        elif len(self.minHeap)-len(self.maxHeap)>1:
            tmp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*tmp)    


    def findMedian(self) -> float:
        if len(self.minHeap)==0 and len(self.maxHeap)==0:
            return None
        
        if len(self.minHeap)==0:
            return -1.0*self.maxHeap[0]
        
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0]+(-1)*self.maxHeap[0]) / 2.0
        elif len(self.maxHeap) > len(self.minHeap):
            return -1.0*self.maxHeap[0]
        else:
            return self.minHeap[0]/1.0
    
if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
