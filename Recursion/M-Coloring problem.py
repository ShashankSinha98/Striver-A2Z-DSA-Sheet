def graphColoring(graph, color, N):
    
    color_taken = [-1] * N

    def _isPossible(node, c):
        edges = graph[node]

        for i in range(N):
            if edges[i]==1 and color_taken[i] != -1 and color_taken[i] == c:
                return False
        
        return True
    
    def _solve(node):
        if node == N:
            return True
        
        for c in range(color):
            if _isPossible(node, c):
                color_taken[node] = c
                ans = _solve(node+1)
                if ans:
                    return True

                color_taken[node] = -1
        
        return False
    
    return _solve(0)
    

if __name__ == "__main__":
    graph = [[0, 1, 1, 1],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [1, 0, 1, 0]]
    
    N = 4
    color = 3
    ans = graphColoring(graph, color, N)
    print(ans)