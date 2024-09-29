from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        curr = []

        def solve(idx, sum):

            if idx == k:
                if sum == n:
                    res.append(curr[:])
                return

            start = 1 if idx == 0 else curr[idx-1] + 1

            for i in range(start, 10):

                if sum + i > n:
                    break

                curr.append(i)
                solve(idx+1, sum+i)
                curr.pop()
        
        solve(0, 0)
        return res
    

if __name__ == "__main__":
    s = Solution()
    k, n = 3, 9
    ans = s.combinationSum3(k, n)
    print(ans)