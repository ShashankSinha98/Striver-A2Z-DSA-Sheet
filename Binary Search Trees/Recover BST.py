from typing import Optional
from cimports import TreeNode
import sys


class Solution:
    def __init__(self):
        self.prev = TreeNode(-sys.maxsize)
        self.curr = None
        self.first = None
        self.second = None


    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def __inorder(root: Optional[TreeNode]):
            if root == None:
                return
            
            __inorder(root.left)
            self.curr = root
            if self.prev.val > self.curr.val:
                if self.second==None:
                    self.first = self.prev
                    self.second = self.curr
                else:
                    self.second = self.curr
            
            self.prev = self.curr
            __inorder(root.right)
        
        self.prev = TreeNode(-sys.maxsize)
        self.curr = None
        self.first = None
        self.second = None
        __inorder(root)

        if self.first!=None and self.second!=None:
            tmp = self.first.val
            self.first.val = self.second.val
            self.second.val = tmp
    

    def inorder(self, root: Optional[TreeNode]):
        if root==None:
            return
        
        self.inorder(root.left)
        print(root.val, end=", ")
        self.inorder(root.right)


if __name__ == "__main__":
    s = Solution()
    r = TreeNode(1, left=TreeNode(3, right=TreeNode(2)))
    s.recoverTree(r)
    s.inorder(r)