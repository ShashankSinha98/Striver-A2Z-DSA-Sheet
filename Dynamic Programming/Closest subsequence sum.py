from typing import List
import sys
from bisect import bisect_left

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def __generateSubsetSum(arr: List[int]) -> List[int]:
            res = set()
            def __recursion(i, total):
                if i==len(arr):
                    res.add(total)
                    return
                
                __recursion(i+1, total+arr[i])
                __recursion(i+1, total)
            __recursion(0, 0)
            return list(res)

        n = len(nums)
        div = n//2 if n&1==0 else n//2+1
        larr, rarr = nums[:div], nums[div:]
        lss, rss = __generateSubsetSum(larr), sorted(__generateSubsetSum(rarr))
        
        min_diff = sys.maxsize
        for li in lss:
            if li <= goal:
                target = goal-li
                rbi = bisect_left(rss, target)
                
                if rbi<len(rss):
                    min_diff = min(min_diff, abs(target-rss[rbi]))
                if rbi > 0:
                    min_diff = min(min_diff, abs(target-rss[rbi-1]))

        return min_diff
    

if __name__ == "__main__":
    s = Solution()
    nums = [1556913,-259675,-7667451,-4380629,-4643857,-1436369,7695949,-4357992,-842512,-118463]
    goal = -9681425
    print(s.minAbsDifference(nums, goal))
        