from TreeNode import TreeNode
from typing import Optional
import sys


class Solution:
    
    def __init__(self) -> None:
        self.maxPathSumVal = -sys.maxsize

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSumVal = -sys.maxsize
        self.__calculate(root)
        return self.maxPathSumVal
    
    def __calculate(self, node: Optional[TreeNode|None]) -> int:
        if node==None:
            return 0
        
        left = self.__calculate(node.left)
        right = self.__calculate(node.right)

        if left < 0:
            left = 0
        
        if right < 0:
            right = 0
        
        self.maxPathSumVal = max((node.val+left+right), self.maxPathSumVal)
        return max(left, right) + node.val

        
if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    r2 = TreeNode(-10, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    r3 = TreeNode(-3)
    r4 = TreeNode(2, left=TreeNode(-1))
    r5 = TreeNode(-10, left=TreeNode(5, left=TreeNode(2, left=TreeNode(-15)), right=TreeNode(-10)), right=TreeNode(-20))
    print(s.maxPathSum(r5))