from TreeNode import TreeNode
from typing import Optional

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        maxWidth = 1
        q = [(root, 0)]
        while len(q)!=0:
            tmp = []
            _, fidx = q[0]
            _, lidx = q[-1]
            maxWidth = max(maxWidth, lidx-fidx+1)
            while len(q)!=0:
                n, i = q.pop(0)
                if n.left!=None:
                    tmp.append((n.left,2*i+1))
                if n.right!=None:
                    tmp.append((n.right,2*i+2))
                
            
            q.extend(tmp)
            
        return maxWidth

if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(1)
    r2 = TreeNode(1, left=TreeNode(2, left=TreeNode(5), right=TreeNode(3)), right=TreeNode(3, right=TreeNode(7)))
    r3 = TreeNode(1, left=TreeNode(3, left=TreeNode(5, left=TreeNode(6))), right=TreeNode(2, right=TreeNode(9, left=TreeNode(7))))
    print(s.widthOfBinaryTree(r3))




