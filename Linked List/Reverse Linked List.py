from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        new_head = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None

        return new_head
    
    
    def display(self, head):
        tmp = head
        while tmp != None:
            print(tmp.val, end = "->")
            tmp = tmp.next
        print()

if __name__ == "__main__":
    s = Solution()

    ll = ListNode(1, next=ListNode(2, next=ListNode(3)))
    nll = s.reverseList(ll)
    s.display(nll)