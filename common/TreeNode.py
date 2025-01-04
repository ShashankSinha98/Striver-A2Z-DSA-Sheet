from typing import Optional
# LC

class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right