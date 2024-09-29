import sys
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num) <= k:
            return "0"
        
        sys.set_int_max_str_digits(10**6)

        st = []
        for c in num:
            while k > 0 and st and st[-1] > c:
                st.pop()
                k-=1
            st.append(c)
        
        st = st[:len(st)-k]
        res = "".join(st)

        return str(int(res)) if res else "0"


if __name__ == "__main__":
    s = Solution()
    num = "1432219"
    k = 3
    print(s.removeKdigits(num, k))