from typing import Optional
from TreeNode import TreeNode

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr  = root

        while curr != None:
            if curr.left!=None:
                tmp = curr.left
                while tmp.right!=None and tmp.right!=curr:
                    tmp = tmp.right
                
                if tmp.right==None:
                    tmp.right = curr
                    curr = curr.left
                else:
                    x = curr.right
                    curr.right = curr.left
                    curr.left = None
                    tmp.right = x
                    curr = x
            else:
                curr = curr.right
    
    def inorder(self, node: TreeNode):
        if node==None:
            return
        
        self.inorder(node.left)
        print(node.val,end=", ")
        self.inorder(node.right)
    

if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(10, left=TreeNode(5))
    r2 = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5, left=TreeNode(6), right=TreeNode(7))), right=TreeNode(3))
    #s.inorder(r1)
    s.flatten(r2)
    s.inorder(r2)