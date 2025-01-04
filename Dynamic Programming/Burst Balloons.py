from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1, *nums, 1]
        def __recursion(i, j):
            if i>j:
                return 0
            
            max_coins = 0
            for k in range(i, j+1):
                tmp = arr[i-1]*arr[k]*arr[j+1] + __recursion(i, k-1) + __recursion(k+1, j)
                max_coins = max(max_coins, tmp)
            
            return max_coins

        dp = {}
        def __top_down(i, j):
            if i>j:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]

            max_coins = 0
            for k in range(i, j+1):
                tmp = arr[i-1]*arr[k]*arr[j+1] + __top_down(i, k-1) + __top_down(k+1, j)
                max_coins = max(max_coins, tmp)
            
            dp[(i, j)] = max_coins
            return max_coins

        return __top_down(1, len(nums))


if __name__ == "__main__":
    s = Solution()
    nums = [1,5]
    print(s.maxCoins(nums))
