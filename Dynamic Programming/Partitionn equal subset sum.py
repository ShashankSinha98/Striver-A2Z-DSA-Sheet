from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1 > 0:
            return False
        
        target = total//2
    
        def __recursion(arr, n, t):
            if t==0:
                return True
            if n==0:
                return False
            
            if arr[n-1]<=t:
                return __recursion(arr, n-1, t-arr[n-1]) or __recursion(arr, n-1, t)
            else:
                return __recursion(arr, n-1, t)
        
        dp = [[-1]*(target+1) for i in range(n+1)]
        def __top_down(arr, n, t):
            if t==0:
                return True
            if n==0:
                return False
            
            if dp[n][t]!=-1:
                return dp[n][t]
            
            if arr[n-1]<=t:
                dp[n][t] = __top_down(arr, n-1, t-arr[n-1]) or __top_down(arr, n-1, t)
            else:
                dp[n][t] = __top_down(arr, n-1, t)
            return dp[n][t]
    
        return __top_down(nums, len(nums), target)