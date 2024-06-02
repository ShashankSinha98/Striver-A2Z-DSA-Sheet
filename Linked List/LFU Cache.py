from typing import Optional


class DLLNode:
    def __init__(self, key: Optional[int]=None, value: Optional[int]=None) -> None:
        self.key = key
        self.value = value
        self.prev: Optional[DLLNode] = None
        self.next: Optional[DLLNode] = None
        self.count = 1

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

    def __str__(self) -> str:
        res = ""
        tmp = self.head.next

        while tmp != self.tail:
            res+= f"(k: {tmp.key}, v: {tmp.value}, c: {tmp.count}) => "
            tmp = tmp.next
        return res

    # def display(self):
    #     tmp = self.head.next

    #     while tmp != self.tail:
    #         print(f"(k:{tmp.key}, v:{tmp.value}, c:{tmp.count})", end=" => ")
    #         tmp = tmp.next
    #     print()

class LFUCache:

    def __init__(self, capacity: int):
        self.freq_dll_dict : dict[int, DLL] = {}
        self.key_node_dict: dict[int, DLLNode] = {}
        self.capacity = capacity
        self.least_freq: int = 0


    def get(self, key: int) -> int:
        if key not in self.key_node_dict:
            return -1
        
        node = self.key_node_dict[key]
        self.freq_dll_dict[node.count].remove_node(node)
        if node.count == self.least_freq and self.freq_dll_dict[node.count].size == 0:
            self.least_freq = node.count + 1
        
        node.count += 1

        if node.count not in self.freq_dll_dict:
            self.freq_dll_dict[node.count] = DLL()
        
        self.freq_dll_dict[node.count].add_front(node)
        #self.display()
        return node.value
    

    def put(self, key: int, value: int) -> None:
        
        if key in self.key_node_dict:
            node = self.key_node_dict[key]
            self.freq_dll_dict[node.count].remove_node(node)

            if node.count == self.least_freq and self.freq_dll_dict[node.count].size == 0:
                self.least_freq = node.count + 1
            
            node.count += 1
            if node.count not in self.freq_dll_dict:
                self.freq_dll_dict[node.count] = DLL()

            self.freq_dll_dict[node.count].add_front(node)
            node.value = value
            #self.display()
            return
        
        elif len(self.key_node_dict) == self.capacity:
            dll = self.freq_dll_dict[self.least_freq]
            last_node = dll.tail.prev
            dll.remove_node(last_node)
            self.key_node_dict.pop(last_node.key)

        new_node = DLLNode(key, value)
        self.key_node_dict[key] = new_node
        if 1 not in self.freq_dll_dict:
            self.freq_dll_dict[1] = DLL()
        
        self.freq_dll_dict[1].add_front(new_node)
        self.least_freq = 1
        #self.display()
    

    def display(self):
        for k, v in self.freq_dll_dict.items():
            print(f"{k}: {v}")


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(3,1)
    lfu.put(2,1)
    lfu.put(2,2)
    lfu.put(4,4)
    print("*")
    print(lfu.get(2))