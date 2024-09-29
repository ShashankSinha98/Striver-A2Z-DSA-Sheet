from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def _noOfSubarrLTEGoal(goal: int) -> int:
            l, r = 0, 0
            odd_count = 0
            subarray_count = 0

            while r < len(nums):
                if nums[r] & 1 != 0:
                    odd_count += 1
                
                while odd_count > goal:
                    if nums[l] & 1 != 0:
                        odd_count -= 1
                    l += 1
                
                subarray_count += (r-l+1)
                r+=1
            
            return subarray_count

        return _noOfSubarrLTEGoal(k) - _noOfSubarrLTEGoal(k-1)


if __name__ == "__main__":
    s = Solution()
    nums = [2,2,2,1,2,2,1,2,2,2]
    k = 2
    print(s.numberOfSubarrays(nums, k))
