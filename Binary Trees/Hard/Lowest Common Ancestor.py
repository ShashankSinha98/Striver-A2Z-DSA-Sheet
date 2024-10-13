class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root==None:
            return None
        elif root==p:
            return p
        elif root==q:
            return q
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left==None and right==None:
            return None
        elif left==None:
            return right
        elif right==None:
            return left
        else:
            return root
        
