from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ps, f, s = None, head, head
        while f != None and f.next != None:
            ps = s
            s = s.next
            f = f.next.next
        
        ps = ps.next.next
        return head

