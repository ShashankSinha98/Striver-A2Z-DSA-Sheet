class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        st = [i for i in range(n)]

        while len(st) >= 2:
            a = st.pop()
            b = st.pop()

            if M[a][b] == 1:
                st.append(b)
            else:
                st.append(a)

        poss_celeb = st.pop()

        return poss_celeb if self.confirm_celeb(M, n, poss_celeb) else -1

    def confirm_celeb(self, M, n, poss_celeb):

        for i in range(n):
            if ((M[poss_celeb][i]!=0) or (i!=poss_celeb and M[i][poss_celeb]!=1)):
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    M = [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
    n = len(M)
    print(s.celebrity(M, n))