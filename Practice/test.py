from typing import List


class Solution:
    
    inversionCount = 0
    def numberOfInversions(self, a : List[int], n : int) -> int:
        global inversionCount
        inversionCount = 0

        def _merge_sort(a: List[int], left: int, right: int):
            if left < right:
                
                mid = int(left + (right - left) / 2)
                
                _merge_sort(a, left, mid)
                _merge_sort(a, mid+1, right)
                _merge(a, left, mid, right)
            
    
        def _merge(a: List[int], left: int, mid: int, right: int):
            global inversionCount

            lSize = mid-left+1
            rSize = right-mid

            larr = [0] * lSize
            rarr = [0] * rSize

            for i in range(left, mid+1):
                larr[i-left] = a[i]
            
            for j in range(mid+1, right+1):
                rarr[j-mid-1] = a[j]
            
            i, j, k = 0, 0, left
            # count rev pairs
            while i < lSize and j < rSize:
                if larr[i] > 2*rarr[j]:
                    inversionCount+= lSize-i
                    j+=1
                else:
                    i+=1
                
            # normal merge sort
            i, j, k = 0, 0, left
            while i < lSize and j < rSize:
                if larr[i] <= rarr[j]:
                    a[k] = larr[i]
                    i+=1
                else:
                    a[k] = rarr[j]
                    j+=1

                k+=1
            
            while i < lSize:
                a[k] = larr[i]
                k+=1
                i+=1

            while j < rSize:
                a[k] = rarr[j]
                k+=1
                j+=1

        _merge_sort(a, 0, n-1)
        return inversionCount
    
    def reversePairs(self, nums: List[int]) -> int:
        return self.numberOfInversions(nums, len(nums))


if __name__ == "__main__":
    s = Solution()
    arr = [1,3,2,3,1]
    print(s.reversePairs(arr))