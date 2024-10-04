from TreeNode import *
from typing import Optional, List

class Solution:
    # L Ro R
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        st = []
        res = []

        while len(st) != 0 or node!=None:
            # go left
            while node != None:
                st.append(node)
                node = node.left
            
            n = st.pop()
            res.append(n.val)
            node = n.right
        return res


if __name__ == "__main__":
    s = Solution()
    n = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))
    res = s.inorderTraversal(n)
    print(res)