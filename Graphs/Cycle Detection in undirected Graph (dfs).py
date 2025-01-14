from typing import List
class Solution:
	#Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		visited = [False]*V

		def __recursion(node, parent):
			visited[node]=True
			ans = False
			for ni in adj[node]:
				if not visited[ni]:
					ans = ans | __recursion(ni, node)
				else: # visited
					if ni != parent: # visited neighbour of node is not its parent
						return True
			return ans

		ans = False
		for n in range(V):
			if not visited[n]:
				ans = ans | __recursion(n, -1)
		return ans

if __name__ == "__main__":
	s = Solution()
	adj = [[1], [0]]
	V = len(adj)

	print(s.isCycle(V, adj))