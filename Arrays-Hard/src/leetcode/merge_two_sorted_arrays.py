from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i, j = m-1, 0

        while i >= 0 and j < n:
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                i-=1
                j+=1
            else:
                break
        
        i, j = m, 0
        while i < (m+n):
            nums1[i] = nums2[j]
            j+=1
            i+=1
        
        nums1.sort()

if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    s.merge(nums1, 3, nums2, len(nums2))
    print(nums1)