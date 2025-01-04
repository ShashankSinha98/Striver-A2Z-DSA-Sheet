from typing import List

class Solution:
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        
        if n<=1:
            return n
        
        left_lis = [1]*n
        right_lis = [1]*n

        for i in range(1, n):
            for j in range(i):
                if nums[j]<nums[i] and left_lis[j]+1>left_lis[i]:
                    left_lis[i] = left_lis[j]+1
        
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[j]<nums[i] and right_lis[j]+1>right_lis[i]:
                    right_lis[i] = right_lis[j]+1

        res=0
        for i in range(n):
            if left_lis[i]>1 and right_lis[i]>1:
                res = max(res, left_lis[i]+right_lis[i]-1)
        return res
    
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lbs = self.LongestBitonicSequence(len(nums), nums)
        return len(nums)-lbs
    
if __name__ == "__main__":
    s = Solution()
    nums = [2,1,1,5,6,2,3,1]
    print(s.minimumMountainRemovals(nums))