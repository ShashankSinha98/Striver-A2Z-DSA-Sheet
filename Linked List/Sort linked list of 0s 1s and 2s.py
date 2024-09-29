
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        


def sortList(head):
    zero_head, one_head, two_head = None, None, None
    tmp_zero, tmp_one, tmp_two = None, None, None
    tmp = head
    display(head)

    while tmp != None:
        if tmp.data == 0:
            if tmp_zero == None:
                zero_head = tmp_zero = tmp
                tmp = tmp.next
            else:
                tmp_zero.next = tmp
                tmp_zero = tmp
                tmp = tmp.next
                tmp_zero.next = None
        elif tmp.data == 1:
            if tmp_one == None:
                one_head = tmp_one = tmp
                tmp = tmp.next
            else:
                tmp_one.next = tmp
                tmp_one = tmp
                tmp = tmp.next
                tmp_one.next = None
        else:
            if tmp_two == None:
                two_head = tmp_two = tmp
                tmp = tmp.next
            else:
                tmp_two.next = tmp
                tmp_two = tmp
                tmp = tmp.next
                tmp_two.next = None

    #display(zero_head)
    #display(one_head)
    #display(two_head)
    
    new_head = None
    if tmp_zero != None:
        new_head = zero_head
        
        if one_head != None:
            tmp_zero.next = one_head
            tmp_one.next = two_head
        else:
            tmp_zero.next = two_head
    elif tmp_one != None:
        new_head = one_head
        tmp_one.next = two_head
    else:
        new_head = two_head
    
    #display(new_head)
    return new_head

def display(head):
    tmp = head
    while tmp != None:
        print(tmp.data, end = "->")
        tmp = tmp.next
    print()

if __name__ == "__main__":
    l1 = Node(1, Node(0, Node(2, Node(1, Node(0, Node(2, Node(1)))))))
    ans = sortList(l1)
    #display(ans)


