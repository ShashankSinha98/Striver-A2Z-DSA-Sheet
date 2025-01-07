from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        def __recursion(i, j):
            if i>j:
                return 0
            
            max_sum = 0
            max_till_now = 0
            for ki in range(i, min(i+k, n)):
                max_till_now = max(max_till_now, arr[ki])
                tmp = max_till_now * (ki-i+1) + __recursion(ki+1, j)
                max_sum = max(max_sum, tmp)
            return max_sum
        
        dp = {}
        def __top_down(i, j):
            if i>j:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            max_sum = 0
            max_till_now = 0
            for ki in range(i, min(i+k, n)):
                max_till_now = max(max_till_now, arr[ki])
                tmp = max_till_now * (ki-i+1) + __top_down(ki+1, j)
                max_sum = max(max_sum, tmp)
            dp[(i, j)] = max_sum
            return max_sum
        return __top_down(0, n-1)


if __name__ == "__main__":
    s = Solution()
    arr = [20779,436849,274670,543359,569973,280711,252931,424084,361618,430777,136519,749292,933277,477067,502755,695743,413274,168693,368216,677201,198089,927218,633399,427645,317246,403380,908594,854847,157024,719715,336407,933488,599856,948361,765131,335089,522119,403981,866323,519161,109154,349141,764950,558613,692211]
    k = 26
    print(s.maxSumAfterPartitioning(arr, k))
