from TreeNode import TreeNode
from typing import List, Optional

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderDict = {}
        for i in range(len(inorder)):
            inorderDict[inorder[i]] = i
        
        return self.build(inorderDict, postorder, 0, len(inorder)-1)

    def build(self, inorderDict: dict[int, int], postorder: List[int], stIdx: int, endIdx: int) -> Optional[TreeNode|None]:
        #print(f"po: {postorder}, stidx: {stIdx}, enidx: {endIdx}")

        if len(postorder)==0:
            return None
        
        pl = len(postorder)
        val = postorder[pl-1]
        node = TreeNode(val)

        pos = inorderDict[val]
        leftLen = pos-stIdx
        rightLen = endIdx-pos

        rightPostorder = postorder[pl-rightLen-1: pl-1]
        leftPostorder = postorder[pl-rightLen-leftLen-1: pl-rightLen-1]

        node.left = self.build(inorderDict, leftPostorder, stIdx, pos-1)
        node.right = self.build(inorderDict, rightPostorder, pos+1, endIdx)
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
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    
    r2 = s.buildTree(inorder, postorder)
    s.inorder(r2)
