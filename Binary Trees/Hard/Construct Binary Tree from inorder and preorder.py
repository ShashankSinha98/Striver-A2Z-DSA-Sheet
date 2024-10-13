from TreeNode import TreeNode
from typing import List, Optional

class Solution:
    def __init__(self):
        self.inorderIdx = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorderIdx = 0
        inorderDict = {}
        for i in range(len(inorder)):
            inorderDict[inorder[i]] = i

        return self.build2(preorder, inorderDict, 0, len(inorder)-1)
    

    def build2(self, preorder: List[int], inorderDict: dict[int, int], stIdx: int, endIdx: int) -> Optional[TreeNode]:
        print(f"pr: {preorder}, st: {stIdx}, en: {endIdx}")
        if len(preorder)==0:
            return None

        val = preorder[0]
        node = TreeNode(val)

        pos = inorderDict[val]
        leftLen = pos-stIdx
        rightLen = endIdx-pos

        node.left = self.build2(preorder[1:leftLen+1], inorderDict, stIdx, pos-1)
        node.right = self.build2(preorder[leftLen+1: leftLen+1+rightLen], inorderDict, pos+1, endIdx)
        return node
    
    def inorder(self, node: TreeNode):
        if node==None:
            return
        
        self.inorder(node.left)
        print(node.val,end=", ")
        self.inorder(node.right)
        
if __name__ == "__main__":
    r1 = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5, left=TreeNode(6), right=TreeNode(7))), right=TreeNode(3))
    s = Solution()
    preorder = [1,2,4,5,6,7,3]
    inorder = [4,2,6,5,7,1,3]
    r2 = s.buildTree(preorder, inorder)
    s.inorder(r2)
