from typing import Optional
from cimports import TreeNode

import sys


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def __validate(root: Optional[TreeNode], min: int, max: int) -> bool:
            if root==None:
                return True
            
            cRoot = min<root.val and root.val<max
            if not cRoot:
                return False
            lAns = __validate(root.left, min, root.val)
            rAns = __validate(root.right, root.val, max)
            return lAns and rAns
        
        return __validate(root, -sys.maxsize, sys.maxsize)