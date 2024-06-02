from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0 
        zero_count, max_len = 0, 0
        inc = True

        while l < len(nums) and r < len(nums):
            
            if inc:
                num = nums[r]
                if num == 0:
                    zero_count += 1

                if zero_count <= k:
                    max_len = max(max_len, r-l+1)
                    r+=1
                else:
                    inc = False
            else:
                num = nums[l]
                l+=1

                if num==0:
                    zero_count -= 1
                
                if zero_count <=k:
                    inc = True
                    r+=1
            
        return max_len
    

if __name__ == "__main__":
    s = Solution()
    print(s.longestOnes(nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3))