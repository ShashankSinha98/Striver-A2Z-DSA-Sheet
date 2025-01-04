from cimports import Node

class Solution:
    def floor(self, root: Node, x: int):
        
        if root == None:
            return -1

        elif root.data == x:
            return x
        
        else:
            if root.data < x:
                ans = self.floor(root.right, x)
                return root.data if ans==-1 else ans
            else:
                ans = self.floor(root.left, x)
                return -1 if ans==-1 else ans

if __name__ == "__main__":
    s = Solution()
    r1 = Node(2, right=Node(81, left=Node(42, right=Node(66, left=Node(45))), right=Node(87, right=Node(90))))
    print(s.floor(r1, 1))