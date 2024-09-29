class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, h = 0, (n*m)-1

        while l <= h:
            x = (l+h) // 2

            r, c = x//m, x%m
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                h = x - 1
            else:
                l = x + 1

        return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3

    print(Solution().searchMatrix(matrix, target))