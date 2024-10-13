from typing import Optional, List

class Node:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def Paths(self, root : Optional[Node]) -> List[List[int]]:
        res = []
        self.__paths(root, [], res)
        return res

    def __paths(self, node: Optional[Node], tmp: List[int], res: List[List[int]]):
        if node==None:
            return
        
        if node.left==None and node.right==None:
            tmp.append(node.data)
            res.append(tmp.copy())
            tmp.pop()
            return
        
        tmp.append(node.data)
        self.__paths(node.left, tmp, res)
        self.__paths(node.right, tmp, res)
        tmp.pop()


if __name__ == "__main__":
    s = Solution()
    r1 = Node(10, left=Node(20, left=Node(40), right=Node(60)), right=Node(30))
    print(s.Paths(r1))