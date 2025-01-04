class Solution:
    def isSubsetSum (self, arr, target):
        def __recursion(arr, n, t):
            if t==0:
                return True
            if n==0:
                return False
            
            if arr[n-1]<=t:
                return __recursion(arr, n-1, t-arr[n-1]) or __recursion(arr, n-1, t)
            else:
                return __recursion(arr, n-1, t)
        return __recursion(arr, len(arr), target)


if __name__ == "__main__":
    s = Solution()
    arr = [3, 34, 4, 12, 5, 2]
    t = 30
    print(s.isSubsetSum(arr, t))