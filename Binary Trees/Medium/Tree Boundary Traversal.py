class Solution:
    def printBoundaryView(self, root):
        childs=[]
        if root.left!=None or root.right!=None:
            self.getChildrens(root, childs)

        left, right = [], []
        if root.left !=None:
            self.getLefts(root.left, left)
        if root.right!=None:
            self.getRights(root.right, right)
            right.reverse()
        

        res = [root.data]
        res.extend(left)
        res.extend(childs)
        res.extend(right)
    
        return res

    def getChildrens(self, root, res):
        if root==None:
            return
        
        if root.left==None and root.right==None:
            res.append(root.data)
            return
        
        self.getChildrens(root.left, res)
        self.getChildrens(root.right, res)
    
    def getLefts(self, root, res):
        if root==None:
            return
        
        if root.left==None and root.right==None:
            return
        
        res.append(root.data)
        if root.left!=None:
            self.getLefts(root.left, res)
        else:
            self.getLefts(root.right, res)

    def getRights(self, root, res):
        if root==None:
            return
        
        if root.left==None and root.right==None:
            return
        
        res.append(root.data)
        if root.right!=None:
            self.getRights(root.right, res)
        else:
            self.getRights(root.left, res)

class Node:
    def __init__(self, val, left=None, right=None):
        self.right = right
        self.data = val
        self.left = left
    
    def __str__(self) -> str:
        return f"Node({self.data})"

if __name__ == "__main__":
    s = Solution()
    r1 = Node(1)
    r2 = Node(1, left=Node(2),right=Node(3))
    r3 = Node(1, left=Node(2, left=Node(4), right=Node(5, left=Node(8), right=Node(9))), right=Node(3, left=Node(6), right=Node(7)))
    r4 = Node(1,left=Node(2, left=Node(4, left=Node(6), right=Node(5)), right=Node(9, right=Node(3, left=Node(7), right=Node(8)))))
    r5 = Node(1, left=Node(2, left=Node(3,right=Node(4,left=Node(5),right=Node(6)))), right=Node(7,right=Node(8,left=Node(9,left=Node(10),right=Node(11)))))
    print(s.printBoundaryView(r1))
