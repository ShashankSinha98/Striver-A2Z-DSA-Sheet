class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c_arr = [0] * 26

        for i in range(len(s)):

            s_idx = ord(s[i]) - ord('a')
            c_arr[s_idx] += 1

            t_idx = ord(t[i]) - ord('a')
            c_arr[t_idx] -= 1

        
        for i in range(len(c_arr)):
            if c_arr[i] != 0:
                return False
        
        return True


if __name__ == "__main__":
    s = "rat"
    t = "car"

    print(Solution().isAnagram(s, t))