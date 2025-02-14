 
class Solution:
    def preToInfix(self, pre_exp):
        st = []
        n = len(pre_exp)

        for i in range(n-1, -1, -1):
            c = pre_exp[i]

            if c not in ['-', '+', '*', '/', '^']:
                st.append(c)
            else:
                op1 = st.pop()
                op2 = st.pop()
                res = "("+op1+c+op2+")"
                st.append(res)
        
        res = st.pop()
        return res


if __name__ == "__main__":
    s = Solution()
    exp = "*-A/BC-/AKL"
    print(s.preToInfix(exp))