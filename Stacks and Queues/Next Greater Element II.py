from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        st = []
        i = 2*len(nums) - 1

        while i >= 0:
            idx = i % len(nums)
            if len(st) == 0:
                res.append(-1)
                st.append(nums[idx])
                i-=1
            
            elif st[len(st)-1] > nums[idx]:
                res.append(st[len(st)-1])
                st.append(nums[idx])
                i-=1
            
            else:
                st.pop()
        
        res = res[::-1]
        return res[:len(nums)]


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,3]
    print(s.nextGreaterElements(nums))