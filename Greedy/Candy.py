from typing import List


class Solution:
    def candy2(self, ratings: List[int]) -> int:
        total, i, n = 1, 1, len(ratings)

        while i < n:
            if ratings[i]==ratings[i-1]:
                total+=1
                i+=1
            else:
                inc = 1
                while i < n and ratings[i] > ratings[i-1]:
                    inc+=1
                    total+=inc
                    i+=1
                
                dec = 0
                while i<n and ratings[i] < ratings[i-1]:
                    dec+=1
                    total+=dec
                    i+=1
                
                if dec+1 > inc:
                    total+=(dec-inc+1)
        
        return total
    
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        tmp=[1]*n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                tmp[i] = tmp[i-1]+1
        
        res = 0
        last = 1
        for i in range(n-1, -1, -1):
            if i==n-1 or ratings[i]<=ratings[i+1]:
                last = 1
            else:
                last += 1
            res += max(tmp[i], last)

        return res
    


if __name__ == "__main__":
    s = Solution()
    ratings = [5,4,3,1,4,5]
    ans = s.candy2(ratings)
    print(ans)
        