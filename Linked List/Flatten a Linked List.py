class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.

def merge(left_head: Node, right_head: Node) -> Node:
    
    p1, p2 = left_head, right_head
    new_head = None

    while p1 != None and p2 != None:
        if p1.data < p2.data:
            if new_head == None:
                new_head = p1
            else:
                new_head.child = p1
                new_head = p1
            p1 = p1.child
        else:
            if new_head == None:
                new_head = p2
            else:
                new_head.child = p2
                new_head = p2
            p2 = p2.child
    
    if p1 != None:
        new_head.child = p1
    else:
        new_head.child = p2
    
    return left_head if left_head.data < right_head.data else right_head


def flattenLinkedList(head: Node) -> Node:
    if head == None or head.next == None:
        return head
    merge_head = flattenLinkedList(head.next)
    return merge(head, merge_head)