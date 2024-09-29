class Solution:
    def convertMinToMaxHeap(self, N, arr):
        lastNonLeafNodeIdx = (N-1)//2

        for idx in range(lastNonLeafNodeIdx, -1, -1):
            self.heapifyDown(idx, arr)

    def heapifyDown(self, idx, arr):
        while(not self.isLeaf(idx, len(arr))):    
            leftChildIdx = 2*idx + 1
            rightChildIdx = 2*idx + 2
            largestElementIdx = idx

            if leftChildIdx < N and arr[leftChildIdx] > arr[idx]:
                largestElementIdx = leftChildIdx
            
            if rightChildIdx < N and arr[rightChildIdx] > arr[largestElementIdx]:
                largestElementIdx = rightChildIdx
            
            if largestElementIdx == idx:
                break

            arr[largestElementIdx], arr[idx] = arr[idx], arr[largestElementIdx]
            idx = largestElementIdx

    def isLeaf(self, idx: int, N: int) -> bool:
        return (2*idx > N-1)
        




if __name__ == "__main__":
    s = Solution()
    arr = [3,5,9,6,8,20,10,12,8,9]
    N = len(arr)
    s.convertMinToMaxHeap(N, arr)
    print(arr)