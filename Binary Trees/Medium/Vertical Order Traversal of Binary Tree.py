from TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        map = {}
        self.__verticalMapping(root,0, 0, map)
        cols = list(map.keys())
        col_st = min(cols)

        res = []
        for c in range(col_st, col_st+len(cols)):
            rows = list(map[c].keys())
            rows.sort()
            tmp = []
            for r in rows:
                map[c][r].sort()
                tmp.extend(map[c][r])
            res.append(tmp)
        
        return res

    def __verticalMapping(self, node: TreeNode, row: int, col: int, map: dict[int, dict[int, list[int]]]):
        if node==None:
            return
        
        if col not in map:
            map[col] = {}
        if row not in map[col]:
            map[col][row] = []
        
        map[col][row].append(node.val)

        self.__verticalMapping(node.left, row+1, col-1, map)
        self.__verticalMapping(node.right,row+1, col+1, map)


if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(1)
    r2 = TreeNode(1, left=TreeNode(2),right=TreeNode(3))
    r21 = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))
    r3 = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5, left=TreeNode(8), right=TreeNode(9))), right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))
    r4 = TreeNode(1,left=TreeNode(2, left=TreeNode(4, left=TreeNode(6), right=TreeNode(5)), right=TreeNode(9, right=TreeNode(3, left=TreeNode(7), right=TreeNode(8)))))
    r5 = TreeNode(1, left=TreeNode(2, left=TreeNode(3,right=TreeNode(4,left=TreeNode(5),right=TreeNode(6)))), right=TreeNode(7,right=TreeNode(8,left=TreeNode(9,left=TreeNode(10),right=TreeNode(11)))))

    print(s.verticalTraversal(r2))
