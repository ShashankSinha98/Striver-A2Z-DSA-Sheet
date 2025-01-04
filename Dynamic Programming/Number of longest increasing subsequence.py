from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        count=[1]*n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lis[j]+1 > lis[i]:
                        lis[i] = lis[j]+1
                        count[i] = count[j]
                    elif lis[j]+1 == lis[i]:
                        count[i] += count[j]
        
        max_lis = max(lis)
        total = 0
        for i in range(n):
            if lis[i]==max_lis:
                total+=count[i]
        return total


if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,4]
    #nums = [2,2,2,2,2]
    #nums = [1]
    print(s.findNumberOfLIS(nums))
        