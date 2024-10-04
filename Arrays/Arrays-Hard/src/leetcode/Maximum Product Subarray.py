from typing import List
import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix = 1, 1
        n = len(nums)
        max_prod = -sys.maxsize
        
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n-i-1]

            max_prod = max(max_prod, prefix, suffix)

            if prefix==0:
                prefix=1
            
            if suffix==0:
                suffix=1    

        
        return max_prod


if __name__ == "__main__":
    s = Solution()
    nums = [2,3,-2,4]
    print(s.maxProduct(nums))
