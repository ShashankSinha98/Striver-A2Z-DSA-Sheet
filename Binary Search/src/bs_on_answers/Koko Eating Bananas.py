import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        l, r = 1, max(piles)
        ans = r
        while l <= r:
            m = l + (r-l)//2
            #print(l, m, r)
            hours_req = 0
            for pi in piles:
                hours_req += math.ceil(pi/m)
            
            if hours_req > h:
                l = m + 1
            else:
                ans = min(ans, m)
                r = m - 1
        
        return ans
    

if __name__ == "__main__":
    arr = [312884470]
    h = 312884469
    ans = Solution().minEatingSpeed(arr, h)
    print(ans)
        