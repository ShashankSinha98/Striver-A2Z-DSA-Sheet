from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = []

        for i in range(len(nums)-2):
            
            if i!=0 and nums[i] == nums[i-1]: # skip duplicate no
                continue

            j,k = i+1, len(nums)-1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total==0:
                    ans = [nums[i],nums[j],nums[k]]
                    res.append(ans)
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]: # skip duplicate no
                        j+=1
                    while j < k and nums[k] == nums[k+1]: # skip duplicate no
                        k-=1

                elif total > 0:
                    k-=1
                else:
                    j+=1
        
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    res = s.threeSum(nums)
    print("res: ",res)
