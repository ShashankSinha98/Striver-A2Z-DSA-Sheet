class Solution:
    def count(self, n):
        if n<=2:
            return n
        
        edge_count = n*(n-1)//2
        return 2**edge_count
    