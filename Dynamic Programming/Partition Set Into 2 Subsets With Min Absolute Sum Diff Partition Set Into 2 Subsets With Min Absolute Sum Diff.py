from typing import List
import sys

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        def __recursion(i, fSum, fLen):
            if i==n:
                sSum = sum(nums)-fSum
                return abs(fSum-sSum)

            take = sys.maxsize
            if fLen < n//2:
                if n-i > (n//2-fLen):
                    take = __recursion(i+1, fSum+nums[i], fLen+1)
                    notTake = __recursion(i+1, fSum, fLen)
                    return min(take, notTake)
                else:
                    take = __recursion(i+1, fSum+nums[i], fLen+1)
                    return take
            else:
                notTake = __recursion(i+1, fSum, fLen)
                return notTake
            
        dp = {}
        def __top_down(i, fSum, fLen):
            if i==n:
                sSum = sum(nums)-fSum
                return abs(fSum-sSum)

            if (i, fSum, fLen) in dp:
                return dp[(i, fSum, fLen)]
            
            take = sys.maxsize
            if fLen < n//2:
                if n-i > (n//2-fLen):
                    take = __top_down(i+1, fSum+nums[i], fLen+1)
                    notTake = __top_down(i+1, fSum, fLen)
                    dp[(i, fSum, fLen)] = min(take, notTake)
                else:
                    take = __top_down(i+1, fSum+nums[i], fLen+1)
                    dp[(i, fSum, fLen)] = take
            else:
                notTake = __top_down(i+1, fSum, fLen)
                dp[(i, fSum, fLen)] = notTake
            
            return dp[(i, fSum, fLen)]
        
        return __top_down(0, 0, 0)

if __name__ == "__main__":
    s = Solution()
    nums = [2,-1,0,4,-2,-9]    # ans = 0
    print(s.minimumDifference(nums))
        