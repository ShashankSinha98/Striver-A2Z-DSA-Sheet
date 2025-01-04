from typing import List, Optional
from cimports import TreeNode
import sys

class Solution:
    pos = 0
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        global pos 
        pos = 0
        def __build(min: int, max: int) -> Optional[TreeNode]:
            global pos
            if pos==len(preorder):
                return None
            
            d = preorder[pos]
            if d > max or d < min:
                return None
            
            nn = TreeNode(d)
            pos+=1
            nn.left = __build(min, d)
            nn.right = __build(d, max)
            return nn

        return __build(-sys.maxsize, sys.maxsize)
    
    def inorder(self, root: Optional[TreeNode]):
        if root==None:
            return
        
        self.inorder(root.left)
        print(root.val, end=", ")
        self.inorder(root.right)


if __name__ == "__main__":
    s = Solution()
    preorder = [8,5,1,7,10,12]
    r = s.bstFromPreorder(preorder)
    s.inorder(r)
    