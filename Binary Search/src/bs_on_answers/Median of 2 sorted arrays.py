import sys

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len2 < len1:
            return self.findMedianSortedArrays(nums2, nums1)
        
        # corner cases
        if len1 == 0 and len2 == 0:
            return 0.0
        elif len1==0:
            return self.median(nums2)
        elif len2==0:
            return self.median(nums1)
        
        low, high = 0, len1

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = ((len1+len2+1)//2) - cut1

            l1 = nums1[cut1-1] if cut1-1 >=0 else -sys.maxsize
            l2 = nums2[cut2-1] if cut2-1 >=0 else -sys.maxsize

            r1 = nums1[cut1] if cut1 < len1 else sys.maxsize
            r2 = nums2[cut2] if cut2 < len2 else sys.maxsize
            #print(cut1, cut2)
            #print(l1, l2, r1, r2)
            if l1 <= r2 and l2 <= r1:
                if (len1+len2) & 1 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        
        return 0.0
    
    def median(self, arr: list[int]) -> float:
        n = len(arr)
        mid = (n+1) // 2
        if n & 1 == 0:
            return (arr[mid-1]+arr[mid])/2.0
        else:
            return arr[mid-1]

if __name__ == "__main__":
    nums2 = [1, 2]
    nums1 = [3, 4]

    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print(ans)
        