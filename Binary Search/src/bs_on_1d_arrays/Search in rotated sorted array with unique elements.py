from typing import List

class Solution:
    def search(self, arr: List[int], K: int) -> int:
        l, r = 0, len(arr)-1

        while l <= r:
            mid = int(l + (r-l)/2)

            if arr[mid] == K:
                return mid
            elif arr[l] <= arr[mid]:  # left is sorted
                if arr[l] <= K <= arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # right is sorted
                if arr[mid] <= K <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
    
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    tar = 3

    s = Solution()
    print(s.search(nums, tar))
