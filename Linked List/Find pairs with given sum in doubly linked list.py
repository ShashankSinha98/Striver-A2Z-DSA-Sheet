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

def get_len(head: Node) -> int:
        tmp = head
        if tmp == None:
            return 0
        count = 1
        tmp = head
        while tmp.next != None:
            count += 1
            tmp = tmp.next
        
        return count

def findPairs(head: Node, k: int) -> [[int]]:

    res = []
    tail, n = get_tail(head), get_len(head)
    th, tt = head, tail
    l, r = 0, n-1

    while l < r:
        s = th.data + tt.data
        #print(s, l, r)
        if s == k:
            res.append([th.data, tt.data])
            th = th.next
            tt = tt.prev
            l += 1
            r -= 1
        elif s < k:
            th = th.next
            l += 1
        else:
            tt = tt.prev
            r -= 1
    
    return res