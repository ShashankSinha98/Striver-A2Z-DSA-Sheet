from typing import List

class Solution:
    def __init__(self) -> None:
        self.last_pos = -1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)
        self.last_pos = N - 1

        for i in range(N//2-1, -1, -1):
            self.heapify_max_down(i, nums, N)
        
        for i in range(k-1):
            self.pop(nums)
        
        return self.pop(nums)
        

    def heapify_max_down(self, i: int, nums: List[int], N: int):
        if i > N//2 - 1:
            return
        
        left = 2*i+1
        right = 2*i+2

        largest = i
        if left < N and nums[left] > nums[i]:
            largest = left
        
        if right < N and nums[right] > nums[largest]:
            largest = right

        if largest == i:
            return
        
        nums[largest], nums[i] = nums[i], nums[largest]
        self.heapify_max_down(largest, nums, N)

    def pop(self, nums) -> int:
        if self.last_pos == -1:
            return None
        
        res = nums[0]
        nums[0] = nums[self.last_pos]
        self.last_pos-=1
        self.heapify_max_down(0, nums, self.last_pos+1)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1,5,6,4]
    k = 6
    ans = s.findKthLargest(nums, k)
    print(ans)