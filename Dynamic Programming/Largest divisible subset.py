from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #nums.sort()
        lds = [1]*n
        hash = [i for i in range(n)]
        max_len, max_len_idx = 1, 0

        for i in range(1, n):
            for j in range(i):
                if (nums[i] % nums[j]==0 or nums[j] % nums[i]==0) and lds[j]+1>lds[i]:
                    lds[i] = lds[j]+1
                    hash[i] = j
                    if lds[i] > max_len:
                        max_len = lds[i]
                        max_len_idx = i
        
        ans = []
        idx = max_len_idx
        ans.append(nums[idx])

        while hash[idx]!=idx:
            idx = hash[idx]
            ans.append(nums[idx])
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [4,8,10,240]
    print(s.largestDivisibleSubset(nums))
