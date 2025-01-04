class Node:
    def __init__(self, val, left=None, right=None):
        self.right = right
        self.data = val
        self.left = left

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        map = {}
        self.__verticalMapping(root, 0, 0, map)
        cols = list(map.keys())
        st_col = min(cols)
        res = []

        for ci in range(st_col, st_col+len(cols)):
            rows = list(map[ci].keys())
            r = min(rows)
            res.append(map[ci][r][0])
        return res

    def __verticalMapping(self, node, row, col, map):
        if node==None:
            return
        
        if col not in map:
            map[col] = {}
        if row not in map[col]:
            map[col][row] = []
        
        map[col][row].append(node.data)

        self.__verticalMapping(node.left, row+1, col-1, map)
        self.__verticalMapping(node.right,row+1, col+1, map)

if __name__ == "__main__":
    s = Solution()
    r1 = Node(1)
    r2 = Node(1, left=Node(2),right=Node(3))
    r21 = Node(1, left=Node(2, left=Node(4), right=Node(5)),right=Node(3, left=Node(6), right=Node(7)))
    r3 = Node(1, left=Node(2, left=Node(4), right=Node(5, left=Node(8), right=Node(9))), right=Node(3, left=Node(6), right=Node(7)))
    r4 = Node(1,left=Node(2, left=Node(4, left=Node(6), right=Node(5)), right=Node(9, right=Node(3, left=Node(7), right=Node(8)))))
    r5 = Node(1, left=Node(2, left=Node(3,right=Node(4,left=Node(5),right=Node(6)))), right=Node(7,right=Node(8,left=Node(9,left=Node(10),right=Node(11)))))

    print(s.topView(r21))