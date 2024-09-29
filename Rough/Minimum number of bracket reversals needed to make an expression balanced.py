class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for i in str:
            if i=='(':
                st.append(i)
            elif i==')':
                if len(st)>0 and st[-1]=='(':
                    st.pop()
                else:
                    st.append(i)
        return len(st)


if __name__ == "__main__":
    s = Solution()
    str="()))(("
    print(s.minAddToMakeValid(str))