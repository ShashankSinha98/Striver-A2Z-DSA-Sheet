from TreeNode import TreeNode
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        
        leftThenRight=True
        st1, st2 = [root], []
        res = []

        while len(st1)!=0 or len(st2)!=0:
            tmp = []
            if leftThenRight:
                while len(st1)!=0:
                    n=st1.pop()
                    tmp.append(n.val)
                    if n.left!=None:
                        st2.append(n.left)
                    if n.right!=None:
                        st2.append(n.right)
                leftThenRight = False
                res.append(tmp)
            else:
                while len(st2)!=0:
                    n=st2.pop()
                    tmp.append(n.val)
                    if n.right!=None:
                        st1.append(n.right)
                    if n.left!=None:
                        st1.append(n.left)
                leftThenRight = True
                res.append(tmp)
        return res


if __name__ == "__main__":
    s = Solution()
    r = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print(s.zigzagLevelOrder(r))

                    