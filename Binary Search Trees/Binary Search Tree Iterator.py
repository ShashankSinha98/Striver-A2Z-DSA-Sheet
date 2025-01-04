from typing import Optional
from cimports import TreeNode

class BSTIterator1:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.key = -1

    def next(self) -> int:
        suc = self.getSuccessor()
        self.key = suc.val
        return suc.val

    def hasNext(self) -> bool:
        suc = self.getSuccessor()
        return suc != None

    def getSuccessor(self) -> Optional[TreeNode]:
        suc = None
        tmp = self.root
        while tmp != None:
            if tmp.val > self.key:
                suc = tmp
                tmp = tmp.left
            else:
                tmp = tmp.right
        
        return suc

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        tmp = root
        while tmp != None:
            self.st.append(tmp)
            tmp = tmp.left
        

    def next(self) -> int:
        res = self.st.pop()
        if res.right != None:
            tmp = res.right
            while tmp != None:
                self.st.append(tmp)
                tmp = tmp.left
        return res.val

    def hasNext(self) -> bool:
        return len(self.st) > 0


if __name__ == "__main__":
    r = TreeNode(7, left=TreeNode(3), right=TreeNode(15, left=TreeNode(9), right=TreeNode(20)))
    s = BSTIterator(r)
    print(s.next())
    print(s.next())
    print(s.hasNext())
    print(s.next())
    print(s.hasNext())
    print(s.next())
    print(s.hasNext())
    print(s.next())
    print(s.hasNext())