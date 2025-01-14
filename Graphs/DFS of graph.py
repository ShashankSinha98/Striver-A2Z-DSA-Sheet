class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        N = len(adj)
        res, visited = [], [False]*N

        def __recursion(node):
            res.append(node)
            visited[node]=True

            for nbi in adj[node]:
                if visited[nbi]==False:
                    __recursion(nbi)
        
        __recursion(0)
        return res
    
if __name__=="__main__":
    s = Solution()
    adj = [[2,3,1], [0], [0,4], [0], [2]]
    print(s.dfsOfGraph(adj))

