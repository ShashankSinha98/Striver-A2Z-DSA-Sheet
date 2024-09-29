from typing import *
import math

# Approach 1
# def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
#     m, n = len(a), len(b)
#     i, j = m-1, 0

#     while i >= 0 and j < n:
#         if a[i] > b[j]:
#             a[i], b[j] = b[j], a[i]
#             i-=1
#             j+=1
#         else:
#             break

#     a.sort()
#     b.sort()


# Approach 2
def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    m, n = len(a), len(b)
    i = 0
    gap = math.ceil((m+n)/2)

    while gap > 0:
        i, j = 0, gap

        while j < (m+n):
            d1 = a[i] if i < m else b[i-m]
            d2 = a[j] if j < m else b[j-m]

            if d1 > d2:
                if i<m:
                    a[i] = d2
                else:
                    b[i-m] = d2
                
                if j<m:
                    a[j] = d1
                else:
                    b[j-m] = d1
            
            i+=1
            j+=1
        
        if gap != 1:
            gap = math.ceil(gap/2)
        else:
            break
        


if __name__ == "__main__":
    a = [1, 8, 8]
    b = [2, 3, 4, 5]
    mergeTwoSortedArraysWithoutExtraSpace(a,b)
    print(a)
    print(b)