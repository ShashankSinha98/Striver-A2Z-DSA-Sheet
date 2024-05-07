from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def _solve(self, arr: List[int], idx: int, curr: List[int], res: set, sum: int, k: int):

            # base case
            if sum > k:
                return
            
            if idx == len(arr):    
                if sum == k:
                    res.append(curr.copy())
                return

            # 1. take and retain
            curr.append(arr[idx])
            sum += arr[idx]
            _solve(self, arr, idx, curr, res, sum, k)

            # 2. take and move            
            #_solve(self, arr, idx+1, curr, res, sum, k)

            # 3. skip and move
            curr.pop()
            sum -= arr[idx]
            _solve(self, arr, idx+1, curr, res, sum, k)
        
        res = []
        _solve(self, candidates, 0, [], res, 0, target)
        return res
    

if __name__ == "__main__":
    s = Solution()
    candidates = [2, 3, 5]
    target = 6

    ans = s.combinationSum(candidates, target)
    print(ans)