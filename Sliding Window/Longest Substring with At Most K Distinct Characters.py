def LongestSubstringWithAtMostKDistinctCharacters(s: str, k: int) -> int:
    max_len = 0
    l, r = 0, 0
    c_dict = {}

    while r < len(s):
        c = s[r]
        if c not in c_dict:
            c_dict[c] = 1
        else:
            c_dict[c] += 1
        


        while len(c_dict) > k:
            t = s[l]
            l+=1
            c_dict[t] -= 1
            if c_dict[t] == 0:
                c_dict.pop(t)

        max_len = max(max_len, r-l+1)
        r+=1
    
    return max_len


if __name__ == "__main__":
    s = "aaabbccd"
    k = 2
    print(LongestSubstringWithAtMostKDistinctCharacters(s, k))