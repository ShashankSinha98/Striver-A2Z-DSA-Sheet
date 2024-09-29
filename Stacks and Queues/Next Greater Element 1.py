from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt_greater_dict  = {}
        st = []
        i = len(nums2)-1

        while i >= 0:
            if len(st) == 0:
                nxt_greater_dict[nums2[i]] = -1
                st.append(nums2[i])
                i-=1
            
            elif st[len(st)-1] > nums2[i]:
                nxt_greater_dict[nums2[i]] = st[len(st)-1]
                st.append(nums2[i])
                i-=1
            
            else:
                st.pop()
        
        res = []
        for i in nums1:
            res.append(nxt_greater_dict[i])
        
        return res
    

if __name__ == "__main__":
    s = Solution()
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    print(s.nextGreaterElement(nums1, nums2))


