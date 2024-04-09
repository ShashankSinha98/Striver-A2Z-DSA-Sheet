class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.

def get_tail(head: Node) -> Node:
    tmp = head
    if tmp == None:
        return None
    
    tmp = head
    while tmp.next != None:
        tmp = tmp.next
    
    return tmp

def deleteAllOccurrences(head: Node, k: int) -> Node:
    tmp = head
    tail = get_tail(head)
    dh = Node(-1, head, None)
    head.prev = dh
    dt = Node(-1, None, tail)
    tail.next = dt

    while tmp != dt:

        if tmp.data != k:
            tmp = tmp.next
        else:
            prev = tmp.prev
            nxt = tmp.next
            prev.next = nxt
            nxt.prev = prev
            tmp = nxt
        
    if dh.next == dt:
        return None
    else:
        head = dh.next
        tail = dt.prev
        head.prev = tail.next = None
        dh.next = dt.prev = None
        return head

def display(head):
    tmp = head
    print("<-> ", end="")
    while tmp != None:
        print(tmp.data, end = " <-> ")
        tmp = tmp.next
    print()

if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(10, prev=n1)
    n1.next = n2

    display(n1)

    n3 = deleteAllOccurrences(n1, 10)
    display(n3)
    
    

