from TreeNode import *
from typing import Optional, List

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        rightChecked = set()
        stack, res = [], []

        while len(stack)!=0 or node!=None:
            if node==None:
                n = stack.pop()
                res.append(n.val)
            
            while node!=None:
                stack.append(node)
                node = node.left
            
            if len(stack)>0 and stack[-1] not in rightChecked:
                rightChecked.add(stack[-1])
                node = stack[-1].right
        return res
    
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack, res = [], []

        while len(stack)!=0 or curr!=None:            
            if curr!=None:
                stack.append(curr)
                curr = curr.left
            else:
                tmp = stack[-1].right
                if tmp!=None:
                    curr = tmp
                else:
                    tmp = stack.pop()
                    res.append(tmp.val)
                    while len(stack)>0 and stack[-1].right==tmp:
                        tmp = stack.pop()
                        res.append(tmp.val)
        return res
    

if __name__ == "__main__":
    s = Solution()
    n = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))
    res = s.postorderTraversal(n)
    print(res)