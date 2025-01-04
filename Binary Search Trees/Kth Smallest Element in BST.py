from typing import Optional
from cimports import TreeNode

class Solution:
    def kthSmallest(self, r: Optional[TreeNode], k: int) -> int:
        count = k
        result = None
        def __inorder(root: Optional[TreeNode]):
            nonlocal count, result
            if root==None:
                return
            
            __inorder(root.left)
            count-=1
            if count==0:
                result = root.val
                return
            
            __inorder(root.right)
        
        __inorder(r)
        return result
        


if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    print(s.kthSmallest(r1,1))