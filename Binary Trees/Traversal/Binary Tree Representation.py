class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.data = val

    def __str__(self) -> str:
        return str(self.data)


class Solution:
    def createTree(self, root, l):
        def __build(pos, l):
            if pos >= len(l):
                return None
            
            nn = Node(l[pos])
            nn.left = __build(2*pos+1, l)
            nn.right = __build(2*pos+2, l)
            return nn
        
        if root==None:
            return
        
        root.left = __build(1, l)
        root.right = __build(2, l)

    
    def printInorder(self, root):
        if root == None:
            return
        
        self.printInorder(root.left)
        print(root.data, end=", ")
        self.printInorder(root.right)


if __name__ == "__main__":
    s = Solution()
    l = [1,2,3,4,5,6,7]
    r = Node(-1)
    r = s.createTree2(r, l)
    s.printInorder(r)