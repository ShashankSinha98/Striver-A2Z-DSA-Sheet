class Solution:
	def all_longest_common_subsequences(self, s, t):
		def __get_bottom_up_dp():
			ns, nt = len(s), len(t)
			dp = [[0]*(nt+1) for _ in range(ns+1)]
			
			for ni in range(1, ns+1):
				for nj in range(1, nt+1):
					if s[ni-1]==t[nj-1]:
						dp[ni][nj] = 1 + dp[ni-1][nj-1]
					else:
						dp[ni][nj] = max(dp[ni][nj-1], dp[ni-1][nj])
			return dp
		
		ns, nt = len(s), len(t)
		dp = __get_bottom_up_dp()
		ans = set()
		visited = set()
		def __recursion(i, j, r, ans: set):
			if i==0 or j==0:
				ans.add(r)
				return
			
			if (i, j ,r) in visited:
				return
			
			visited.add((i,j,r))
			
			if s[i-1]==t[j-1]:
				__recursion(i-1, j-1, s[i-1]+r, ans)
			else:
				if dp[i][j]==dp[i-1][j]:
					__recursion(i-1, j, r, ans)

				if dp[i][j]==dp[i][j-1]:
					__recursion(i, j-1, r, ans)

		__recursion(ns, nt, "", ans)
		res = list(ans)
		res.sort()
		return res


if __name__ == "__main__":
	sol = Solution()
	s = "abaaa"
	t =  "baabaca"

	print(sol.all_longest_common_subsequences(s, t))
