from TreeNode import TreeNode
from typing import Optional

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        lh = self.__lHeight(root)
        rh = self.__rHeight(root)

        if lh==rh:
            return (2**lh)-1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def __lHeight(self, node: Optional[TreeNode|None]) -> int:
        if node==None:
            return 0
        return 1+self.__lHeight(node.left)
    
    def __rHeight(self, node: Optional[TreeNode|None]) -> int:
        if node==None:
            return 0
        return 1+self.__rHeight(node.right)
    
if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3, left=TreeNode(6)))
    r2 = TreeNode(1)
    print(s.countNodes(r2))