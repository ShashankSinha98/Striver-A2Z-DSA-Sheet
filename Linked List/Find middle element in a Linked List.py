class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMiddle(head: Node):
    # Write your code here
    # head denoted head of linked list
    f, s = head, head
    while f!=None and f.next!=None:
        f = f.next.next
        s = s.next
    return s