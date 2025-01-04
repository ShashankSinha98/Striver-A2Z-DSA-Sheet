from typing import Optional, List
from TreeNode import TreeNode

class Solution:
    # Preorder = Ro, L, Ri 
    # post order = L, Ri, Ro
    # rev - Ro, Ri, L (similar to preorder, just switch left and right)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root

        while curr != None:

            if curr.right==None:
                res.append(curr.val)
                curr = curr.left
            else:
                tmp = curr.right
                while tmp.left!=None and tmp.left!=curr:
                    tmp = tmp.left
                
                if tmp.left==None:
                    res.append(curr.val)
                    tmp.left = curr
                    curr = curr.right
                else:
                    tmp.left = None
                    curr = curr.left
        res.reverse()
        return res

if __name__ == "__main__":
    r1 = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5, left=TreeNode(6), right=TreeNode(7))), right=TreeNode(3))
    s = Solution()
    print(s.postorderTraversal(r1))

        