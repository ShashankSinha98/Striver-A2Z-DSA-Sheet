from cimports import Node
import sys

class Solution:
    class Res:
        def __init__(self, size: int, max: int, min: int):
            self.size = size
            self.max = max
            self.min = min
        
    def largestBst(self, root: Node):
        def __postorder(root: Node) -> Solution.Res:
            if root==None:
                return Solution.Res(0, -sys.maxsize, sys.maxsize)
            
            if root.left==None and root.right==None:
                return Solution.Res(1, root.key, root.key)
            
            leftRes = __postorder(root.left)
            rightRes = __postorder(root.right)

            if leftRes.max < root.key and root.key < rightRes.min:
                size = leftRes.size + rightRes.size + 1
                _max = rightRes.max if rightRes.max!=-sys.maxsize else root.key
                _min = leftRes.min if leftRes.min!=sys.maxsize else root.key
                return Solution.Res(size, _max, _min)
            else:
                return Solution.Res(max(leftRes.size, rightRes.size), sys.maxsize, -sys.maxsize)
        return __postorder(root).size

if __name__ == "__main__":
    s = Solution()
    r = Node(6, left=Node(6, right=Node(2)), right=Node(2, left=Node(1), right=Node(1)))
    print(s.largestBst(r))
