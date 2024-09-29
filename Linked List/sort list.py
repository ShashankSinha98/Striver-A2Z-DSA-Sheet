from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next        
        return slow

    def merge(self, left_head: Optional[ListNode], right_head: Optional[ListNode]) -> Optional[ListNode]:
        
        # if left_head.val > right_head.val:
        #     left_head, right_head = right_head, left_head
        
        # print("LH: ", end="") 
        # self.display(left_head)
        # print("RH: ", end="") 
        # self.display(right_head)
        
        p1, p2 = left_head, right_head
        new_head = None

        while p1 != None and p2 != None:
            if p1.val < p2.val:
                if new_head == None:
                    new_head = p1
                else:
                    new_head.next = p1
                    new_head = p1
                p1 = p1.next
            else:
                if new_head == None:
                    new_head = p2
                else:
                    new_head.next = p2
                    new_head = p2
                p2 = p2.next
        
        if p1 != None:
            new_head.next = p1
        else:
            new_head.next = p2
        
        return left_head if left_head.val < right_head.val else right_head
        

    def display(self, head):
        tmp = head
        while tmp != None:
            print(tmp.val, end = "->")
            tmp = tmp.next
        print()

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        mid = self.middle(head)
        right_head = mid.next
        mid.next = None
        left_head = head

        left_sorted_ll = self.sortList(left_head)
        right_sorted_ll = self.sortList(right_head)
        new_head = self.merge(left_sorted_ll, right_sorted_ll)
        return new_head

        

if __name__ == "__main__":
    odd_ll = ListNode(1)
    even_ll = ListNode(6, ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))

    # sort_1 = ListNode(1, ListNode(3))
    # sort_2 = ListNode(2, ListNode(4, ListNode(6, ListNode(7))))
    # res = Solution().merge(sort_1, sort_2)
    # Solution().display(res)
    ans = Solution().sortList(odd_ll)
    Solution().display(ans)