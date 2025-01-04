
from typing import Optional
from cimports import TreeNode

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            # leaf node
            if root.left==None and root.right==None:
                return None
            # only one child
            elif root.left==None or root.right==None:
                return root.left if root.left!=None else root.right
            # 2 childrens
            else:
                rNode = root.left
                while rNode.right!=None:
                    rNode = rNode.right
                
                root.val = rNode.val
                root.left = self.deleteNode(root.left, rNode.val)
                return root

    def deleteNode2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None
        elif key > root.val:
            root.right = self.deleteNode2(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode2(root.left, key)
            return root
        else:
            # leaf node
            if root.left==None and root.right==None:
                return None
            # only one child
            elif root.left==None or root.right==None:
                return root.left if root.left!=None else root.right
            # 2 childrens
            else:
                rNode = root.right
                tmp = root.left
                while tmp.right!=None:
                    tmp = tmp.right
                
                tmp.right = rNode
                return root.left

    def inOrder(self, root: Optional[TreeNode]):
        if root==None:
            return
        
        self.inOrder(root.left)
        print(root.val, end=", ")
        self.inOrder(root.right)


if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(10, left=TreeNode(5, left=TreeNode(3, left=TreeNode(1)), right=TreeNode(9)), right=TreeNode(15))
    s.inOrder(r1) 
    print()
    r1 = s.deleteNode2(r1, 5)
    s.inOrder(r1)

        