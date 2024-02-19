class Solution:
    def total_bouquet_possible(self, bloomDay: list[int], k: int, day: int) -> int:
        possible_bouquet_count = 0
        adj_bloom_flower_count = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                adj_bloom_flower_count += 1
                
                if adj_bloom_flower_count == k:
                    possible_bouquet_count += 1
                    adj_bloom_flower_count = 0
            else:
                adj_bloom_flower_count = 0
        
        return possible_bouquet_count

    
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k > len(bloomDay): # no. of flowers requires is less than available
            return -1
        
        l, r = min(bloomDay), max(bloomDay)
        ans = r

        while l <= r:
            day = l + (r-l) // 2
            total_bouquet_possible = self.total_bouquet_possible(bloomDay, k, day)
            if total_bouquet_possible >= m:
                ans = min(ans, day)
                r = day - 1
            else:
                l = day + 1
        
        return ans

if __name__ == "__main__":
    bloomDay = [7,7,7,7,12,7,7]
    m, k = 2, 3
    ans = Solution().minDays(bloomDay, m, k)
    print(ans)