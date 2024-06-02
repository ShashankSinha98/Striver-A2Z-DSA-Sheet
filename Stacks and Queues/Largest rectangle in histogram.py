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


if __name__ == "__main__":
    s = Solution()
    heights = [2,4]
    print(s.largestRectangleArea(heights))

