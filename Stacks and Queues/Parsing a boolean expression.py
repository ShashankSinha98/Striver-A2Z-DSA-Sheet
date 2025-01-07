class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        st = []
        i = 0

        while i < len(exp):
            if exp[i]!=')':
                st.append(exp[i])
                i+=1
            else:
                res_set = set()
                while len(st)>0:
                    tmp = st.pop()
                    if tmp == '(':
                        break
                    elif tmp == 't' or tmp == 'f':
                        res_set.add(tmp)
                    else:
                        continue
                
                sign = st.pop()
                if sign=='!':
                    if 't' in res_set:
                        st.append('f')
                    else:
                        st.append('t')
                elif sign=='&':
                    if 'f' in res_set:
                        st.append('f')
                    else:
                        st.append('t')
                else:
                    if 't' in res_set:
                        st.append('t')
                    else:
                        st.append('f')
                i+=1
        return True if st[-1]=='t' else False
    
if __name__ == "__main__":
    s = Solution()
    exp = "!(&(f,t))"
    print(s.parseBoolExpr(exp))