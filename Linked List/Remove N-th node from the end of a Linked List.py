from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2, cnt = head, head, 0
        while p2 != None and cnt < n:
            p2 = p2.next
            cnt += 1

        if cnt != n:
            return None
        
        if p2 == None:
            rem = head
            head = head.next
            return rem
        else:
            while p2.next != None:
                p1 = p1.next
                p2 = p2.next
            
            rem = p1.next
            p1.next = p1.next.next
            return rem