import sys

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        st_idx, min_len = -1, sys.maxsize
        l, r = 0, 0
        count = 0
        t_arr = [0] * 255
        for ti in t:
            t_arr[ord(ti)]+=1
        
        while r < len(s):
            c = ord(s[r])
            if t_arr[c] > 0:
                count += 1
            
            t_arr[c] -= 1

            while count == len(t):
                if r-l+1 < min_len:
                    min_len = r-l+1
                    st_idx = l
                
                tmp = ord(s[l])
                l+=1
                t_arr[tmp] += 1
                if t_arr[tmp] > 0:
                    count -= 1
            r+=1
        
        return "" if st_idx==-1 else s[st_idx:st_idx+min_len]


if __name__ == "__main__":
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s, t))
