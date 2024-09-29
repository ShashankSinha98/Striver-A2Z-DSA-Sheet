from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def length(self, head: ListNode) -> int:
        tmp = head
        cnt = 0
        while tmp != None:
            cnt += 1
            tmp = tmp.next
        
        return cnt
    

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = self.length(headA)
        l2 = self.length(headB)

        diff = 0
        big_head, small_head = None, None
        if l1 > l2:
            diff = l1 - l2
            big_head = headA
            small_head = headB
        else:
            diff = l2 - l1
            big_head = headB
            small_head = headA

        while diff != 0:
            big_head = big_head.next
            diff -= 1

        while big_head != None and small_head != None:
            if big_head == small_head:
                return big_head

            big_head = big_head.next
            small_head = small_head.next

        return None 
        