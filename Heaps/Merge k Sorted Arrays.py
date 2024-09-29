class Node:
    def __init__(self, val: int, arrId: int, pos: int) -> None:
        self.val = val
        self.arrId = arrId
        self.pos = pos


class MinHeap:
    def __init__(self, minHeapSize: int) -> None:
        self.heapArr = []
    
    def insert(self, element: int, arrId: int, pos: int):
        
        nn = Node(element, arrId, pos)
        
        # insert element at last
        self.heapArr.append(nn)
        currPos = len(self.heapArr) - 1

        while(currPos > 0):
            parentIdx = (currPos-1)//2

            if self.heapArr[parentIdx].val > self.heapArr[currPos].val:
                self.heapArr[parentIdx], self.heapArr[currPos] = self.heapArr[currPos], self.heapArr[parentIdx]
                currPos = parentIdx
            else:
                break

    def pop(self) -> Node:
        
        # Replace root with last element
        res = self.heapArr[0]
        self.heapArr[0] = self.heapArr[-1]
        self.heapArr.pop()

        currPos = 0
        # Move new root element at correct position
        while(1):
            smallestElementIdx = currPos
            left = 2*currPos+1
            right = 2*currPos+2

            if left < len(self.heapArr) and self.heapArr[left].val < self.heapArr[currPos].val:
                smallestElementIdx = 2*currPos + 1
            
            if right < len(self.heapArr) and self.heapArr[right].val < self.heapArr[smallestElementIdx].val:
                smallestElementIdx = 2*currPos + 2
            
            if smallestElementIdx==currPos:
                break
            
            self.heapArr[currPos], self.heapArr[smallestElementIdx] = self.heapArr[smallestElementIdx], self.heapArr[currPos]
            currPos = smallestElementIdx

        return res



class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        mh = MinHeap(K)

        for i in range(K):
            mh.insert(arr[i][0], i, 0)
        
        res = [-1] * (K*K)
        tmp = 0
        while tmp < len(res):
            n = mh.pop()
            res[tmp] = n.val
            tmp += 1

            if n.pos+1 == K:
                continue
            else:
                mh.insert(arr[n.arrId][n.pos+1], n.arrId, n.pos+1)
        
        return res


if __name__ == "__main__":
    s = Solution()
    arr = [[1,2,3,4],
           [2,2,3,4],
           [5,5,6,6],
           [7,8,9,9]]

    ans = s.mergeKArrays(arr, 4)
    print(ans)