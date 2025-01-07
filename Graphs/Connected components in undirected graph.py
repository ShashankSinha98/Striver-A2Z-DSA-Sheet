from typing import List

class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        res = [[]*V for _ in range(V)]

        for st, end in edges:
            res[st].append(end)
            res[end].append(st)

        return res
    # Function to return connected components of the graph
    def connectedcomponents(self, v, edges):
        adj_list = self.printGraph(v, edges)
        visited = [False]*v
        tmp = []

        def __rec_visit(node):
            if visited[node]:
                return
            
            tmp.append(node)
            visited[node]=True
            adj_nodes = adj_list[node]
            for i in adj_nodes:
                __rec_visit(i)
        
        res = []
        for ni in range(v):
            if visited[ni]==False:
                tmp = []
                __rec_visit(ni)
                res.append(tmp.copy())
        return res
    

if __name__ == "__main__":
    s = Solution()
    v=5
    edges = [[0, 1],[2, 1],[3, 4]]
    print(s.connectedcomponents(v, edges))

        
