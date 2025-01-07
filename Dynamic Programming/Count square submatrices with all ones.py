from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        dp = [[0]*c for _ in range(r)]
        total = 0

        for ri in range(r):
            dp[ri][0] = matrix[ri][0]
            total += dp[ri][0]

        for ci in range(1, c):
            dp[0][ci] = matrix[0][ci]
            total += dp[0][ci]

        for ri in range(1, r):
            for ci in range(1, c):
                if matrix[ri][ci]==1:
                    dp[ri][ci] = min(dp[ri-1][ci], dp[ri][ci-1], dp[ri-1][ci-1]) + 1
                    total += dp[ri][ci]
        return total
    

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,0,1],[1,1,0],[1,1,0]]
    print(s.countSquares(matrix))