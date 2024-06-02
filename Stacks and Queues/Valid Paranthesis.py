class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c == '(' or c=='{' or c=='[':
                st.append(c)
            else:
                if len(st)==0:
                    return False
                
                top = st[len(st)-1]
                if (c==')' and top!='(') or (c=='}' and top!='{') or (c==']' and top!='['):
                    return False
                
                st.pop()

        return len(st) == 0

if __name__ == "__main__":
    str = "([]"
    s = Solution()
    print(s.isValid(str))