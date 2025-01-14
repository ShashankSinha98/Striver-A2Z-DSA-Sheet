from typing import List

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        r, c = len(grid), len(grid[0])
        for i in range(r):
            if i&1==0:
                st, end, inc = 0, c, 1
            else:
                st, end, inc = c-1, -1, -1

            for j in range(st, end, inc):
                if (i+j)&1==0:
                    res.append(grid[i][j])
        return res


if __name__ == "__main__":
    s = Solution()
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.zigzagTraversal(grid))