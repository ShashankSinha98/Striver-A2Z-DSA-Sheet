import sys

class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        n, m = len(mat), len(mat[0])
        l, h = 0, m-1

        while l <= h:
            mid = (l+h) // 2

            max_idx = 0
            max_no = mat[max_idx][mid]
            for i in range(n):
                if mat[i][mid] > max_no:
                    max_no = mat[i][mid]
                    max_idx = i
            
            left = mat[max_idx][mid-1] if mid-1>=0 else -sys.maxsize
            right = mat[max_idx][mid+1] if mid+1<m else -sys.maxsize

            if mat[max_idx][mid] > left and mat[max_idx][mid] > right:
                return [max_idx, mid]
            elif mat[max_idx][mid] < left:
                h = mid - 1
            else:
                l = mid + 1
        
        return [-1, -1]
    
if __name__ == "__main__":
    mat = [[10,20,15],[21,30,14],[7,16,32]]
    ans = Solution().findPeakGrid(mat)
    print(ans)