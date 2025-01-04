from typing import List
import sys

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def __recursion(i, lastIdx): # TLE
            if i==n:
                return 0
            
            if lastIdx==-1 or nums[lastIdx]<nums[i]:
                return max(1+__recursion(i+1, i), __recursion(i+1, lastIdx))
            else:
                return __recursion(i+1, lastIdx)
        
        dp = {}
        def __top_down(i, lastIdx): # memory limit exceeded
            if i==n:
                return 0
            
            if (i, lastIdx) in dp:
                return dp[(i, lastIdx)]
            
            if lastIdx==-1 or nums[lastIdx]<nums[i]:
                dp[(i, lastIdx)] = max(1+__top_down(i+1, i), __top_down(i+1, lastIdx))
            else:
                dp[(i, lastIdx)] = __top_down(i+1, lastIdx)
            return dp[(i, lastIdx)]
        
        def __bottom_up():
            n = len(nums)
            dp = [[0]*(n+1) for _ in range(n+1)]

            for i in range(n-1, -1,-1):
                for li in range(i-1, -2, -1):
                    if li==-1 or nums[li]<nums[i]:
                        dp[i][li+1] = max(1+dp[i+1][i+1], dp[i+1][li+1])
                    else:
                        dp[i][li+1] = dp[i+1][li+1]
            
            return dp[0][0]
        
        def __smart_way():
            dp = [1]*n
            for i in range(1, n):
                for j in range(i):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[i], dp[j]+1)
            return max(dp)
        
        def __binary_search(_nums):
            def __correct_pos(ni, si, arr): # find upper bound
                l, r = 0, si
                res = r

                while l<=r:
                    m = (l+r)//2
                    if arr[m]==ni:
                        return m
                    elif arr[m]<ni:
                        l = m+1
                    else:
                        res = m
                        r = m-1
                return res

            si, i, n  = 0, 1, len(_nums)
            while i < n:
                if _nums[i]>_nums[si]:
                    _nums[si+1] = _nums[i]
                    si+=1
                    i+=1
                else:
                    p = __correct_pos(_nums[i], si, _nums)
                    _nums[p] = _nums[i]
                    i+=1
            return si+1
        return __binary_search(nums)

if __name__ == "__main__":
    s = Solution()
    nums =  [7,7,7,7,7,7,7]
    print(s.lengthOfLIS(nums))