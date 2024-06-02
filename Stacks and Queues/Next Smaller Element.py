from typing import List

class Solution:
    def prevSmaller(self, nums: List[int]) -> List[int]:
        st = []
        res = []
        i = 0
          
        while i  < len(nums):
            if len(st) == 0:
                res.append(-1)
                st.append(nums[i])
                i+=1
            
            elif st[len(st)-1] < nums[i]:
                res.append(st[len(st)-1])
                st.append(nums[i])
                i+=1
            
            else:
                st.pop()
        
        return res

if __name__ == "__main__":
     s = Solution()
     nums = [4, 5, 2, 10, 8]
     print(s.prevSmaller(nums))
			