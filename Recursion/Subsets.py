from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def _subsets(self, nums: List[int], curr: List[int], res: List[List[int]]):

            if len(nums) == 0:
                res.append(curr.copy())
                return
            
            curr.append(nums[0])
            _subsets(self, nums[1:], curr, res)
            curr.pop()
            _subsets(self, nums[1:], curr, res)
        
        res = []
        _subsets(self, nums, [], res)
        return res
    

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    ans = s.subsets(nums)
    print(ans)