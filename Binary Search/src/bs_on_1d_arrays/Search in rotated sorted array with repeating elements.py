from typing import List

class Solution:
    def search(self, arr: List[int], K: int) -> bool:
        l, r = 0, len(arr)-1

        while l <= r:
            mid = int(l + (r-l)/2)

            if arr[mid] == K:
                return True
            
            # unique case in repeating rotated array [3,1,2,3,3,3,3], l=0, m=3, r=6
            # cannot define whether left or right part is sorted
            elif arr[l] == arr[mid] == arr[r]: 
                l += 1
                r -= 1
                continue

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
        
        return False
    
if __name__ == "__main__":
    nums = [2,5,6,0,0,1,2]
    tar = 3

    s = Solution()
    print(s.search(nums, tar))