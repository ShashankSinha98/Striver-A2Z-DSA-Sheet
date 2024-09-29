class Solution:
    def postToInfix(self, postfix):
        st = []
        n = len(postfix)

        for i in range(n):
            c = postfix[i]

            if c not in ['-', '+', '*', '/', '^']:
                st.append(c)
            else:
                op2 = st.pop()
                op1 = st.pop()
                res = "("+op1+c+op2+")"
                st.append(res)
        
        res = st.pop()
        return res


if __name__ == "__main__":
    s = Solution()
    exp = "ab*c+"
    print(s.postToInfix(exp))