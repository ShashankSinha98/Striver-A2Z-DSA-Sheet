"""
    Time Complexity: O(N * M)
    Space Complexity: O(1)

    Where N is the number of rows and M is the number of columns in the given matrix.
"""
import sys

def rowWithMax1s(matrix: list[list[int]], n: int, m: int) -> int:
    def _count(arr: list[int]):
        l, h = 0, len(arr)-1
        one_idx = sys.maxsize

        while l <= h:
            m = (l + h) // 2

            if arr[m] == 1:
                one_idx = min(m, one_idx)
                h = m - 1
            else:
                l = m + 1
        
        if one_idx == sys.maxsize:
            return 0
        else:
            return len(arr) - one_idx

    max_ones, res_idx = 0, -1
    for i in range(len(matrix)):
        arr = matrix[i]
        ones_count = _count(arr)

        if ones_count > max_ones:
            max_ones = ones_count
            res_idx = i

    return res_idx


if __name__ == "__main__":
    matrix = [     [ 0, 0, 1, 1, 1 ],
      [ 0,  0, 0, 1, 1 ],
      [ 0,  1,  1, 1, 1 ],
         [0,0,0,0,0],
            [ 0,  1,  1, 1, 1 ]   ]
    
    n, m = len(matrix), len(matrix[0])
    print(rowWithMax1s(matrix, n, m))