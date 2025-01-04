from cimports import Node

class Solution:
    def findCeil(self,root: Node, inp: int) -> int:
        if root.data==inp:
            return inp
        
        elif root.data < inp:
            if root.right != None:
                return self.findCeil(root.right, inp)
            else:
                return -1
        
        else:
            ans = -1
            if root.left != None:
                ans = self.findCeil(root.left, inp)
            
            if ans == -1:
                ans = root.data
            return ans

if __name__ == "__main__":
    s = Solution()
    t1 = Node(5, left=Node(1,right=Node(2, right=Node(3))), right=Node(7))
    t2 = Node(10, left=Node(5, left=Node(4), right=Node(7, right=Node(8))), right=Node(11))
    print(s.findCeil(t1, 3))
    print(s.findCeil(t2, 6))