from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        curr = []
        nums.sort()

        def _solve(idx):

            for i in range(idx, len(nums)):
                if i  > idx and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                res.append(curr[:])
                _solve(i+1)
                curr.pop()
        _solve(0)
        return res
    

if __name__ == "__main__":
    s = Solution()
    nums = [0]
    ans = s.subsetsWithDup(nums)
    print(ans)