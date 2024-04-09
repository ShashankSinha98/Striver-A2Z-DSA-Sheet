class Solution:
    def frequencySort(self, s: str) -> str:
        ch_dict = {}

        for ch in s:
            if ch in ch_dict:
                ch_dict[ch] += 1
            else:
                ch_dict[ch] = 1
        
        sorted_dict = sorted(ch_dict.items(), key=lambda item: item[1], reverse=True)
        res = ""
        for k, v in sorted_dict:
            res += k*v
        return res

if __name__ == "__main__":
    s = "loveleetcode"
    print(Solution().frequencySort(s))