import sys
from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        def __recursion(i, j, _cuts):
            if len(_cuts)==0:
                return 0
            
            min_cost = sys.maxsize
            for ci in range(len(_cuts)):
                cut = _cuts[ci]
                tmp = __recursion(i, cut, _cuts[:ci]) + __recursion(cut, j, _cuts[ci+1:]) + (j-i)
                min_cost = min(min_cost, tmp)
            return min_cost

        dp = {}
        def __top_down(i, j, _cuts):
            if len(_cuts)==0:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            min_cost = sys.maxsize
            for ci in range(len(_cuts)):
                cut = _cuts[ci]
                tmp = __top_down(i, cut, _cuts[:ci]) + __top_down(cut, j, _cuts[ci+1:]) + (j-i)
                min_cost = min(min_cost, tmp)
            dp[(i, j)] = min_cost
            return min_cost
        
        return __top_down(0, n, cuts)
        
    
    def __print2D(self,arr):
        n, m = len(arr), len(arr[0])
        for i in range(n):
            for j in range(m):
                print(arr[i][j], end=", ")
            print()


if __name__ == "__main__":
    s = Solution()
    cuts = [1,3,4,5]
    n = 7
    print(s.minCost(n, cuts))
