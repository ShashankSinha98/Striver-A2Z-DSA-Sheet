class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = {}
        char_map_arr = [False] * 1000
        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]
            if ch_s not in mapping:
                if char_map_arr[ord(ch_t)] == True:
                    return False
                mapping[ch_s] = ch_t
                char_map_arr[ord(ch_t)] = True
            else:
                val = mapping[ch_s]
                if val != ch_t:
                    return False
        
        return True

if __name__ == "__main__":
    s = "13"
    t = "42"
    print(Solution().isIsomorphic(s, t))