from typing import List
from queue import Queue


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [False]*N
        
        def bfsOfGraph(node) -> List[int]:
            q = Queue()
            q.put(node)
            visited[node] = True

            res = []
            while q.empty()==False:
                ni = q.get()
                res.append(ni)
                
                for nbi in range(N):
                    if isConnected[ni][nbi]==1 and visited[nbi]==False:
                        q.put(nbi)
                        visited[nbi]=True

            return res
        
        count = 0
        for ni in range(N):
            if visited[ni]==False:
                bfsOfGraph(ni)
                count+=1
        return count
    

if __name__ == "__main__":
    s = Solution()
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(s.findCircleNum(isConnected))