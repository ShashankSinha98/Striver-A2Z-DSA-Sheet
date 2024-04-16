from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for ni in range(1<<n):
            tmp = []

            for j in range(n):
                if (ni & (1<<j)) != 0:
                    tmp.append(nums[j])
            
            res.append(tmp)
        
        return res

    def xor(self, n):
        res = 0
        for i in range(n+1):
            res = res ^ i
        return res
if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    #res = s.subsets(nums)
    for i in range(15):
        res = s.xor(i)
        print(res)