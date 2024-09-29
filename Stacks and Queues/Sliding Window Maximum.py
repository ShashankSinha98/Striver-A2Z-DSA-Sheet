from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dequeue, res = [], []
        i = 0

        while i < len(nums):

            if len(dequeue) == 0 or nums[dequeue[-1]] >= nums[i]:
                dequeue.append(i)
            else:
                dequeue.pop()
                continue

            if dequeue[0] < i-k+1:
                dequeue = dequeue[1:]

            if i >= k-1:
                res.append(nums[dequeue[0]])
                        
            i+=1
        
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1,3,1,2,0,5]
    k = 3
    print(s.maxSlidingWindow(nums, k))
            