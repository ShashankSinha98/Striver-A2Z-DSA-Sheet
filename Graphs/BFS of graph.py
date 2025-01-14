from typing import List
from queue import Queue

#User function Template for python3
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        q = Queue()
        N = len(adj)
        
        visited = [False]*N
        q.put(0)
        visited[0] = True

        res = []
        while q.empty()==False:
            ni = q.get()
            res.append(ni)
            
            for nbi in adj[ni]:
                if visited[nbi]==False:
                    q.put(nbi)
                    visited[nbi]=True

        return res


if __name__ == "__main__":
    s = Solution()
    adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
    print(s.bfsOfGraph(adj))
        
