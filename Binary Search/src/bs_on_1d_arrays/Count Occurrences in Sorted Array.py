def count(arr: [int], n: int, x: int) -> int:
    def searchRange(nums: [int], target: int) -> [int]:
        left, right = 0, len(nums)-1

        # Find start
        start = -1
        while left <= right:
            mid = int(left + (right-left)/2)

            if nums[mid] == target:
                start = mid
                right = mid-1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        if start == -1:
            return [-1, -1]
        
        # Find end
        end = -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int(left + (right-left)/2)

            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1

        return [start, end]
    
    srange = searchRange(arr, x)

    if(srange[0]==-1):
        return 0
    else:
        start = srange[0]
        end = srange[1]
        return end-start+1
