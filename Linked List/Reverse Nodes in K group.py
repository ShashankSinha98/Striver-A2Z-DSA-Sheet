from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        prev_node, tmp = head, head.next
        while tmp != None:
            next_node = tmp.next
            tmp.next = prev_node

            if prev_node == head:
                prev_node.next = None

            prev_node = tmp
            tmp = next_node
        
        return prev_node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        res_head, old_tail = None, None
        l = self.get_length(head)

        if k <= 1 or k > l:
            return head
        
        for _ in range(l//k):
            tmp = head
            c = 1

            while c != k:
                tmp = tmp.next
                c += 1
            
            next_temp = tmp.next
            tmp.next = None

            new_head = self.reverse(head)

            if old_tail == None:
                old_tail = head
                res_head = tmp
            else:
                old_tail.next = new_head
                old_tail = head
            
            head = next_temp
        
        old_tail.next = head
        return res_head


    def get_length(self, head: ListNode) -> int:
        if head == None:
            return 0
        
        cnt = 1
        tmp = head
        while tmp.next != None:
            tmp = tmp.next
            cnt += 1
        
        return cnt
        

    def display(self, head):
        tmp = head
        while tmp != None:
            print(tmp.val, end = " -> ")
            tmp = tmp.next
        print()

if __name__ == "__main__":
    ll = ListNode(1, ListNode(2))
    s = Solution()
    s.display(ll)
    res = s.reverseKGroup(ll, k=2)
    s.display(res)

