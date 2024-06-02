from typing import Optional


class DLLNode:
    def __init__(self, key: Optional[int]=None, value: Optional[int]=None) -> None:
        self.key = key
        self.value = value
        self.prev: Optional[DLLNode] = None
        self.next: Optional[DLLNode] = None


class DLL:
    def __init__(self) -> None:
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    

    def add_front(self, node: DLLNode):
        next = self.head.next
        node.prev = self.head
        node.next = next
        self.head.next = node
        next.prev = node
        self.size += 1
    
    def remove_node(self, node: DLLNode):
        if node == None or node==self.head or node==self.tail:
            return
        
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.size -= 1

    def display(self):
        tmp = self.head.next

        while tmp != self.tail:
            print(tmp.value, end=" => ")
            tmp = tmp.next
        print()


class LRUCache:

    def __init__(self, capacity: int):
        self.lru_dict = {}
        self.dll = DLL()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self.lru_dict:
            return -1
        
        node: DLLNode = self.lru_dict[key]
        self.dll.remove_node(node)
        self.dll.add_front(node)
        
        #self.dll.display()
        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.lru_dict:
            node: DLLNode = self.lru_dict[key]
            node.value = value
            self.dll.remove_node(node)
            self.dll.add_front(node)
            return
        
        elif len(self.lru_dict) == self.capacity:
            last_node = self.dll.tail.prev
            self.dll.remove_node(last_node)
            self.lru_dict.pop(last_node.key)
        
        node = DLLNode(key, value)
        self.dll.add_front(node)
        self.lru_dict[key] = node
        
        #self.dll.display()


if __name__ == "__main__":
    lru = LRUCache(2)
    print(lru.get(2))
    lru.put(2, 6)
    lru.put(1, 5)
    lru.put(1, 2)
    print(lru.get(1))
    print(lru.get(2))