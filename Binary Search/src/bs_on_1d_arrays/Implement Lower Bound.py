def lowerBound(nums: [int], n: int, x: int) -> int:
        l, r = 0, n - 1
        ans = n
        while l <= r:
            mid = int(l + (r-l)/2)

            if nums[mid] >= x:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1       
        return ans

nums = [1, 2, 2, 3, 3, 5]
x = 4
print(lowerBound(nums, len(nums), x))