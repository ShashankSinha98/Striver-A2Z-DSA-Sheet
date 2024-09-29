class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 0
        char_dict = [-1]* 256
        max_len = 1
        while l < len(s) and r < len(s):
            c = ord(s[r])
            if char_dict[c] == -1 or char_dict[c] < l:
                char_dict[c] = r
                max_len = max(max_len, r-l+1)
                r+=1
            else:
                l = char_dict[c] + 1
                char_dict[c] = r
                r += 1

        return max_len



if __name__ == "__main__":
    s = Solution()
    str = "tmmzuxt"
    print(s.lengthOfLongestSubstring(str))