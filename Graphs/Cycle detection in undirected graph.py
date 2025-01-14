from typing import List
from collections import deque 

class Solution:
    
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False]*V
        
        q = deque()
        for i in range(V):
            if not visited[i]:
                q.append((i, -1))
                visited[i] = True

                while len(q)!=0:
                    node, nodeParent = q.popleft()

                    for ni in adj[node]:
                        if not visited[ni]:
                            q.append((ni, node))
                            visited[ni]=True
                        else: # ni already visited
                            if ni != nodeParent: # ni is not parent of node
                                return True                
        return False