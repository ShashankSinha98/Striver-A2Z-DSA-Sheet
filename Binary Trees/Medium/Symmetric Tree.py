from TreeNode import TreeNode
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return False

        return self.__checkSymmetry(root.left, root.right)
        
    def __checkSymmetry(self, n1: TreeNode, n2: TreeNode) -> bool:
        if (n1!=None and n2==None) or (n1==None and n2!=None):
            return False
        
        if n1==None and n2==None:
            return True
        
        ans = n1.val==n2.val
        return ans and self.__checkSymmetry(n1.left, n2.right) and self.__checkSymmetry(n1.right, n2.left)


if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(1)
    r2 = TreeNode(1, left=TreeNode(2), right=TreeNode(2))
    r3 = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    r4 = TreeNode(1, left=TreeNode(2, right=TreeNode(3)), right=TreeNode(2, right=TreeNode(3)))
    print(s.isSymmetric(r4))