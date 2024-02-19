import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        if threshold < n:
            return -1
        
        l, r = 1, max(nums)
        ans = r
        while l <= r:
            m = l + (r-l) // 2

            s = 0
            for wi in nums:
                s += math.ceil(wi / m)
            
            if s <= threshold:
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1
        
        return ans


if __name__ == "__main__":
    nums =  [44,22,33,11,1]
    threshold =  5
    ans = Solution().smallestDivisor(nums, threshold)
    print(ans)