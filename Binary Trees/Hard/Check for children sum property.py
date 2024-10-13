class Node:
    def __init__(self,val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        if root==None or (root.left==None and root.right==None):
            return 1
        
        leftChildVal = root.left.data if root.left!=None else 0
        rightChildVal = root.right.data if root.right!=None else 0
        ans = (leftChildVal+rightChildVal==root.data) and (self.isSumProperty(root.left)==1) and (self.isSumProperty(root.right)==1)
        return 1 if ans else 0


if __name__ == "__main__":
    s = Solution()
    r1 = Node(35, left=Node(20,left=Node(15), right=Node(5)), right=Node(15, left=Node(10), right=Node(5)))
    r2 = Node(10, left=Node(10))
    print(s.isSumProperty(r1))

