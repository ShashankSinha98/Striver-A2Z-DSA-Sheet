from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        st, left, i = [], [], 0
        while i < len(heights):
            if len(st)==0:
                st.append(i)
                left.append(0)
                i+=1
            elif heights[st[-1]] < heights[i]:
                left.append(st[-1]+1)
                st.append(i)
                i+=1
            else:
                st.pop()
        
        st, right, i = [], [], len(heights)-1
        while i >= 0:
            if len(st)==0:
                st.append(i)
                right.append(len(heights)-1)
                i-=1
            elif heights[st[-1]] < heights[i]:
                right.append(st[-1]-1)
                st.append(i)
                i-=1
            else:
                st.pop()
        
        right = right[::-1]
        
        res = []
        for i in range(len(heights)):
            res.append((right[i]-left[i]+1) * heights[i])
    
        return max(res)
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        arr = [0]*col

        max_area = 0
        for ri in range(row-1, -1, -1):
            for ci in range(col):
                if matrix[ri][ci]=="0":
                    arr[ci]=0
                else:
                    arr[ci]+=1
            
            curr_max_area = self.largestRectangleArea(arr)
            max_area = max(max_area, curr_max_area)
        return max_area


if __name__ == "__main__":
    s = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(s.maximalRectangle(matrix))
            
        