from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        
        st = [root]
        res = []
        while len(st)!=0:
            n = st.pop()
            res.append(n.val)

            if n.right!=None:
                st.append(n.right)

            if n.left!=None:
                st.append(n.left)
            
        return res
    

if __name__ == "__main__":
    s = Solution()
    n = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    res = s.preorderTraversal(n)
    print(res)