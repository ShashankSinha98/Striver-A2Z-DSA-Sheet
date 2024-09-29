from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next                

class MinHeap:
    def __init__(self) -> None:
        self.heapArr = []
    
    def insert(self, node: ListNode):
        
        # insert element at last
        self.heapArr.append(node)
        currPos = len(self.heapArr) - 1

        while(currPos > 0):
            parentIdx = (currPos-1)//2

            if self.heapArr[parentIdx].val > self.heapArr[currPos].val:
                self.heapArr[parentIdx], self.heapArr[currPos] = self.heapArr[currPos], self.heapArr[parentIdx]
                currPos = parentIdx
            else:
                break

    def pop(self) -> ListNode:
        
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
    
    def size(self) -> int:
        return len(self.heapArr)



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        mh = MinHeap()

        for i in range(k):
            if isinstance(lists[i], ListNode):
                mh.insert(lists[i])
        
        resHead = ListNode()
        tmp = resHead

        while mh.size() != 0:
            pNode = mh.pop()
            tmp.next = pNode
            tmp = pNode

            if pNode.next == None:
                continue
            else:
                mh.insert(pNode.next)
        
        return resHead.next


if __name__ == "__main__":
    s = Solution()
    lists = [[]]
    print(s.mergeKLists(lists))
