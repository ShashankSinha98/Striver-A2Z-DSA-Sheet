from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        leftmax = rightmax = 0

        while left <= right:

            if height[left] <= height[right]:

                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    res += (leftmax - height[left])
                
                left += 1
            
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    res += (rightmax - height[right])

                right -= 1
        
        return res


if __name__ == "__main__":
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))