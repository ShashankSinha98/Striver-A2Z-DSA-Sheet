class Solution:
    
    def isOperand(self, s: str) -> bool:
        operators = ['^', '+', '-', '/', '*', '(', ')']
        return s not in operators

    def score(self, s: str) -> int:
        if s=='^':
            return 2
        elif s=='*' or s=='/':
            return 1
        elif s=='+' or s=='-':
            return 0

        return -1
    
    def checkPrecedence(self, new_item: str, top_item: str) -> int:
        return self.score(new_item) - self.score(top_item)

    #Function to convert an infix expression to a prefix expression.
    def InfixtoPrefix(self, exp):
        i, res, st = len(exp)-1, "", []

        while i >= 0:
            c = exp[i]
            if self.isOperand(c):
                res += c
                i -= 1
            else:

                if len(st)==0 or (st[len(st)-1]==')' and c!='()') or c==')' or (c != '(' and c!=')' and self.checkPrecedence(c, st[len(st)-1])>=0):
                    st.append(c)
                    i-=1
                
                elif c == '(':
                    while st[len(st)-1] != ')':
                        item = st.pop()
                        res += item
                    
                    st.pop()
                    i-=1
                
                elif self.checkPrecedence(c, st[len(st)-1]) < 0:
                    top = st.pop()
                    res += top

        while len(st) != 0:
            top = st.pop()
            res += top
        
        return res[::-1]
    
if __name__ == "__main__":
    s = Solution()
    exp = "K+L-M*N+(O^P)*W/U/V*T+Q"
    ans = s.InfixtoPrefix(exp)
    print(ans)
