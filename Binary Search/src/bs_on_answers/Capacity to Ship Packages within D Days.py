class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = r

        while l <= r:
            c = l + (r-l) // 2
            #print(l, c, r)

            days_req, wt_sum = 0, 0
            for wi in weights:
                wt_sum += wi
                if wt_sum == c:
                    days_req += 1
                    wt_sum = 0
                elif wt_sum > c:
                    days_req += 1
                    wt_sum = wi
            if wt_sum != 0:
                days_req += 1
            #print("dr: ",days_req)
            
            if days_req <= days:
                ans = min(ans, c)
                r = c - 1
            else:
                l = c + 1

        return ans


if __name__ == "__main__":
    s = Solution()

    weights = [1,2,3,1,1]
    days = 4
    ans = s.shipWithinDays(weights, days)
    print(ans)
