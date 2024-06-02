class Solution:
    def satisfyABC(self, arr) -> bool:
        return 0 not in arr
    
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        total = (n*(n+1)) // 2

        count = 0
        l, r = 0, 0
        c_arr = [0]*3

        while r < n:
            c = ord(s[r]) - ord('a')
            c_arr[c]+=1

            while self.satisfyABC(c_arr):
                t = ord(s[l]) - ord('a')
                c_arr[t] -= 1
                l += 1
            
            count += (r-l+1)
            r+=1

        return total - count
    

if __name__ == "__main__":
    s = Solution()
    my_s = "abaabcacb"
    print(s.numberOfSubstrings(my_s))
        