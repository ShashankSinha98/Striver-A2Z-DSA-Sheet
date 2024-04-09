from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    def get_tail_and_len(self, head: ListNode) -> tuple[ListNode, int]:
        if head == None:
            return None, 0
        
        tmp = head
        count = 1
        
        tmp = head
        while tmp.next != None:
            tmp = tmp.next
            count += 1
        
        return tmp, count

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail, n = self.get_tail_and_len(head)
        if n == 0:
            return None
         
        k = k % n

        if k == 0 or n == 0:
            return head
        else:
            tmp = head
            rot = n - k - 1
            while rot != 0:
                tmp = tmp.next
                rot -= 1      
            
            tail.next = head
            head = tmp.next
            tmp.next = None
        return head

    def display(self, head):
        tmp = head
        while tmp != None:
            print(tmp.val, end = " -> ")
            tmp = tmp.next
        print()

if __name__ == "__main__":
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution()
    s.display(ll)

    res = s.rotateRight(ll, 2)
    s.display(res)
