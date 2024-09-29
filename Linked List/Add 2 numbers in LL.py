from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res, tres = None, None
        sum, carry = 0, 0

        p1, p2 = l1, l2
        while p1 != None and p2 != None:
            sum = (p1.val + p2.val + carry) % 10
            carry = (p1.val + p2.val + carry) // 10

            if tres == None:
                res = ListNode(sum)
                tres = res
            else:
                tres.next = ListNode(sum)
                tres = tres.next
            
            p1 = p1.next
            p2 = p2.next
        
        rp = p1 if p1 != None else p2

        while rp != None:
            sum = (rp.val + carry) % 10
            carry = (rp.val + carry) // 10

            if tres == None:
                res = ListNode(sum)
                tres = res
            else:
                tres.next = ListNode(sum)
                tres = tres.next
            
            rp = rp.next
        
        if carry != 0:
            tres.next = ListNode(carry)
            tres = tres.next
            carry = 0
        
        return res


    def display(self, head):
        tmp = head
        while tmp != None:
            print(tmp.val, end = "->")
            tmp = tmp.next
        print()


if __name__ == "__main__":
    l1 = ListNode(9, ListNode(9))
    #l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    l2 = None

    res = Solution().addTwoNumbers(l1, l2)
    Solution().display(res)