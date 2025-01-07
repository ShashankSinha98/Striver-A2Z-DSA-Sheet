from typing import List

class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        res = [[]*V for _ in range(V)]

        for st, end in edges:
            res[st].append(end)
            res[end].append(st)

        return res