from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elem1 = elem2 = -1
        cnt1 = cnt2 = 0

        for ni in nums:
            if cnt1==0 and ni != elem2:
                elem1 = ni
                cnt1 = 1
            elif cnt2==0 and ni != elem1:
                elem2 = ni
                cnt2 = 1
            elif ni==elem1:
                cnt1+=1
            elif ni==elem2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1

        res: List[int] = []
        if(self.getFrequency(nums, elem1) > math.floor(len(nums)/3)):
            res.append(elem1)
    
        if(elem2 != elem1 and self.getFrequency(nums, elem2) > math.floor(len(nums)/3)):
            res.append(elem2)
    
        return res
    
    def getFrequency(self, nums: List[int], elem) -> int:
        cnt = 0
        for ai in nums:
            if ai == elem:
                cnt+=1
        return cnt


if __name__ == "__main__":
    nums = [1,1,1,2,2]
    ans = Solution().majorityElement(nums)
    print(ans)