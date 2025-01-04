from typing import Optional
from cimports import TreeNode

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)
        
        elif root.val < val:
            if root.right==None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        else:
            if root.left==None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
                
        return root