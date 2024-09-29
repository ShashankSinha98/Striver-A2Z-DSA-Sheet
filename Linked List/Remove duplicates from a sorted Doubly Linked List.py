class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def get_tail(head: Node) -> Node:
    tmp = head
    if tmp == None:
        return None
    
    tmp = head
    while tmp.next != None:
        tmp = tmp.next
    
    return tmp

def removeDuplicates(head: Node) -> Node:
    tail = get_tail(head)
    dH = Node(-1, head, None)
    head.prev = dH
    dT = Node(-1, None, tail)
    tail.next = dT

    tmp = head
    while tmp.next != dT:
        nn = tmp.next
        if tmp.data == nn.data:
            prev = tmp.prev
            nxt = tmp.next
            prev.next = nxt
            nxt.prev = prev
            tmp = nxt
        else:
            tmp = tmp.next
    
    head = dH.next
    tail = dT.prev

    head.prev = tail.next = None
    dH.next = dT.prev = None

    return head


def display(head):
    tmp = head
    print("<-> ", end="")
    while tmp != None:
        print(tmp.data, end = " <-> ")
        tmp = tmp.next
    print()

if __name__ == "__main__":
    n1 = Node(2)
    n2 = Node(2, None, n1)
    n1.next = n2
    n3 = Node(2, None, n2)
    n2.next = n3

    res = removeDuplicates(n1)
    display(res)