import sys

def findKRotation(nums : list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2

            mid_elem = nums[m]
            left_elem = -sys.maxsize if m-1 < 0 else nums[m-1]
            right_elem = sys.maxsize if m+1 >= len(nums) else nums[m+1]
            print(left_elem, mid_elem, right_elem)
            if left_elem < mid_elem and mid_elem > right_elem:
                 return m+1
            elif nums[l] > mid_elem:
                 r = m - 1
            else:
                 l = m + 1
        
        return 0


if __name__ == "__main__":
    arr = [35, 43, 45, 1, 2, 9, 12, 13, 19, 20, 26, 28, 29, 32]
    ans = findKRotation(arr)
    print(ans)