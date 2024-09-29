from typing import List

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
        r, c = len(matrix), len(matrix[0])
        res = 0
        tmp = [0]*c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == "1":
                    tmp[j] += 1
                else:
                    tmp[j]= 0
            res = max(res, self.largestRectangleArea(tmp))

        return res


if __name__ == "__main__":
    s = Solution()
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    
    print(s.maximalRectangle(matrix))

