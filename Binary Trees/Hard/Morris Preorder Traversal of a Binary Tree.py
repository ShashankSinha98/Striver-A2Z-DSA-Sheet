from TreeNode import TreeNode
from typing import Optional, List

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        curr = root

        while curr != None:
            if curr.left==None:
                preorder.append(curr.val)
                curr = curr.right
            else:
                tmp = curr.left
                while tmp.right!=None and tmp.right!=curr:
                    tmp = tmp.right
                
                if tmp.right==None:
                    preorder.append(curr.val)
                    tmp.right = curr
                    curr = curr.left
                else:
                    tmp.right = None
                    curr = curr.right
        return preorder

if __name__ == "__main__":
    r1 = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5, left=TreeNode(6), right=TreeNode(7))), right=TreeNode(3))
    s = Solution()
    print(s.preorderTraversal(r1))
        