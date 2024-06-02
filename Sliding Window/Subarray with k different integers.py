from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysCountLTEGoalDistinct(goal: int) -> int:
            if goal < 0:
                return 0
            
            l, r = 0, 0
            c_dict = {}
            count = 0
            while r < len(nums):
                c = nums[r]
                if c not in c_dict:
                    c_dict[c] = 1
                else:
                    c_dict[c] += 1
                
                while len(c_dict) > goal:
                    t = nums[l]
                    l+=1
                    c_dict[t] -= 1
                    if c_dict[t] == 0:
                        c_dict.pop(t)
                
                count += (r-l+1)
                r+=1
            return count
        a = subarraysCountLTEGoalDistinct(k) 
        b = subarraysCountLTEGoalDistinct(k-1) 
        return a - b


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,1,3,4]
    k = 3
    print(s.subarraysWithKDistinct(nums, k))