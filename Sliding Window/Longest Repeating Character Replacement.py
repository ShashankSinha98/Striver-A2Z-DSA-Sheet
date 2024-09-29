class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        char_freq_dict = {}
        l, r = 0, 0
        inc = True
        max_freq = 0
        while r < len(s):
            if inc:
                c = s[r]        
                
                if c not in char_freq_dict:
                    char_freq_dict[c] = 0
                char_freq_dict[c] += 1

                max_freq = max(max_freq, char_freq_dict[c])
                k_req = (r-l+1) - max_freq

                if k_req > k:
                    inc = False
                else:
                    max_len = max(max_len, r-l+1)
                    r+=1
            else:
                c = s[l]
                l+=1
                char_freq_dict[c] -= 1
                inc = True
                r+=1
                # max_freq = 0
                # for key, v in char_freq_dict.items():
                #     if v > max_freq:
                #         max_freq = v

                # k_req = (r-l+1) - max_freq

                # if k_req <=k:
                #     inc = True
                #     r+=1
        
        return max_len


if __name__ == "__main__":
    s = Solution()
    test_s = "ABCCCA"
    k = 1
    print(s.characterReplacement(test_s, k))