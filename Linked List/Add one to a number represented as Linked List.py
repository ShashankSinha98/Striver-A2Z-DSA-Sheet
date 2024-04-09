class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def addOne(head: Node) -> Node:
    r_head = reverse_ll(head)
    #display(r_head)

    tmp = r_head
    res, tres =  None, None
    carry, sum = 0,0
    while tmp != None:
        if tmp == r_head:
            sum = (tmp.data + 1) % 10
            carry = (tmp.data + 1) // 10
        else:
            sum = (tmp.data + carry) % 10
            carry = (tmp.data + carry) // 10

        if tres == None:
            res = Node(sum)
            tres = res
        else:
            tres.next = Node(sum)
            tres = tres.next
        
        tmp = tmp.next
    
    if carry != 0:
        tres.next = Node(carry)
        tres = tres.next
        carry = 0
    
    #display(res)

    return reverse_ll(res)

def reverse_ll(head: Node) -> Node:
    if head == None or head.next == None:
        return head
    
    p1, p2 = head, head.next
    while p2 != None:
        tp = p2.next
        p2.next = p1
        p1 = p2
        p2 = tp
    
    head.next = None
    head = p1
    return head

def display(head):
    tmp = head
    while tmp != None:
        print(tmp.data, end = "->")
        tmp = tmp.next
    print()

if __name__ == "__main__":
    l1 = Node(9, next=Node(9, next=Node(9)))
    l1 = addOne(l1)
    display(l1)