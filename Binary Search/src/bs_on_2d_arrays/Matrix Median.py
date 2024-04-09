import sys

def median(matrix: list[list[int]], m: int, n: int) -> int:
    left = sys.maxsize
    for i in range(m):
        left = min(left, matrix[i][0])
    
    right = -sys.maxsize
    for i in range(m):
        right = max(right, matrix[i][n-1])
    
    ans = -1

    while left <= right:

        mid = (left+right) // 2

        t = (m*n) // 2

        x = less_than_equal_elements_in_matrix(matrix, mid)
        if x > t:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return ans


def less_than_equal_elements_in_matrix(matrix, t):
    total = 0
    m = len(matrix)
    for i in range(m):
        total += upper_bound(matrix[i], t)
    return total

def upper_bound(arr, t):
    l, r = 0, len(arr)-1
    ans = -1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] <= t:
            ans = max(ans, mid)
            l = mid+1
        else:
            r = mid-1

    return ans + 1


if __name__ == "__main__":
    matrix =  [  [4, 10, 14, 17, 37, 42, 44], 
[2, 3, 11, 11, 30, 35, 44], 
[1, 6, 13, 21, 29, 44, 44], 
[24, 25, 30, 36, 38, 40, 43 ],
[4, 5, 6, 8, 25, 30, 41 ]]
    
    m = len(matrix)
    n = len(matrix[0])

    ans = median(matrix, m, n)
    print(ans)
