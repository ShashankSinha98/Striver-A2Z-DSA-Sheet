from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []    
        ds = []
        candidates.sort()

        def solve(idx: int, target: int):
            if target == 0:
                ans.append(ds[:])
                return
            
            for j in range(idx, len(candidates)):

                if j > idx and candidates[j] == candidates[j-1]:
                    continue

                if candidates[j] > target:
                    break

                ds.append(candidates[j])
                solve(j+1, target-candidates[j])
                ds.pop()
        
        solve(0, target)
        return ans
            

if __name__ == "__main__":
    s = Solution()
    arr = [10,1,2,7,6,1,5]
    tar = 8
    ans = s.combinationSum2(arr, tar)
    print(ans)