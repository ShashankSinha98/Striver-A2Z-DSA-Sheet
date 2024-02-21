class Solution:
    def findKthPositiveLinearSolution(self, arr: list[int], k: int) -> int:
        if k < arr[0]:
            return k
        
        ans = arr[0]
        k = k - arr[0] + 1

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1] - 1
            if diff >= k:
                return ans + k
            else:
                ans = arr[i]
                k = k - diff

        return ans + k


    def findKthPositive(self, arr: list[int], k: int) -> int:
        if k < arr[0]:
            return k

        n = len(arr)            
        l, r = 0, n-1

        while l<=r:
            m = l + (r-l)//2
            #print(l, m, r)
            if k > arr[m]-(m+1):
                l = m + 1
            else:
                r = m - 1
        
        #print(l, r)
        if l < n:
            return arr[r] + (k - (arr[r]-(r+1)))
        else:
            return arr[n-1] + (k - (arr[n-1]-n))


if __name__ == "__main__":
    s = Solution()
    arr = [2,3,4,7,11]
    k = 8
    ans = s.findKthPositive(arr, k)
    print(ans)