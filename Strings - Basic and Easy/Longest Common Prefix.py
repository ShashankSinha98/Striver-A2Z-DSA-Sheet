class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]

        first, second = strs[0], strs[1]
        pref = ""
        i = 0
        while i < len(first) and i < len(second):
            if first[i] == second[i]:
                pref += first[i]
                i += 1
            else:
                break
        
        for i in range(2, n):
            text = strs[i]
            j = 0
            while j < len(text) and j < len(pref):
                if pref[j] == text[j]:
                    j+=1
                else:
                    break
            pref = pref[:j]
        
        return pref
    
if __name__ == "__main__":
    strs = ["aaa","aa","aaa"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
