class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here
        return self.checkRecc(0, arr)

    def checkRecc(self, idx: int, arr) -> bool:
        if 2*idx >= len(arr)-1:
            return True
        
        leftAns = self.checkRecc(2*idx+1, arr)
        rightAns = self.checkRecc(2*idx+2, arr)

        return self.isValidMaxHeapNode(idx, arr) and leftAns and rightAns
        


    def isValidMaxHeapNode(self, idx: int, arr) -> bool:
        
        if(idx>len(arr)):
            return True

        leftChildIdx = 2*idx+1
        rightChildIdx = 2*idx+2

        if leftChildIdx < len(arr) and arr[idx] < arr[leftChildIdx]:
            return False
        
        if rightChildIdx < len(arr) and arr[idx] < arr[rightChildIdx]:
            return False
        
        return True


if __name__ == "__main__":
    s = Solution()
    arr = [90, 15, 10, 7, 12, 2]
    print(s.isMaxHeap(arr, len(arr)))