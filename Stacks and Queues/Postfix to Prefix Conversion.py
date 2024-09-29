class Solution:
    def postToPre(self, post_exp):
        st = []
        n = len(post_exp)

        for i in range(n):
            c = post_exp[i]

            if c not in ['-', '+', '*', '/', '^']:
                st.append(c)
            else:
                op2 = st.pop()
                op1 = st.pop()
                res = c+op1+op2
                st.append(res)
        
        res = st.pop()
        return res

if __name__ == "__main__":
    s = Solution()
    exp = "ABC/-AK/L-*"
    print(s.postToPre(exp))