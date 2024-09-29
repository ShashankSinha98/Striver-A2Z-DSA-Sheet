class Solution:
    def __init__(self) -> None:
        self.last_pos = -1

    def kthSmallest(self, nums, k):
        N = len(nums)
        self.last_pos = N - 1

        for i in range(N//2-1, -1, -1):
            self.heapify_min_down(i, nums, N)
        
        for i in range(k-1):
            self.pop(nums)
        
        return self.pop(nums)

    def heapify_min_down(self, i: int, nums, N: int):
        if i > N//2 - 1:
            return
        
        left = 2*i+1
        right = 2*i+2

        smallest = i
        if left < N and nums[left] < nums[i]:
            smallest = left
        
        if right < N and nums[right] < nums[smallest]:
            smallest = right

        if smallest == i:
            return
        
        nums[smallest], nums[i] = nums[i], nums[smallest]
        self.heapify_min_down(smallest, nums, N)

    def pop(self, nums) -> int:
        if self.last_pos == -1:
            return None
        
        res = nums[0]
        nums[0] = nums[self.last_pos]
        self.last_pos-=1
        self.heapify_min_down(0, nums, self.last_pos+1)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 20, 15]
    k = 4
    ans = s.kthSmallest(nums, k)
    print(ans)