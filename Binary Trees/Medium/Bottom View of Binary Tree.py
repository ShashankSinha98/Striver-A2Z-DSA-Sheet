class Node:
    def __init__(self, val, left=None, right=None):
        self.right = right
        self.data = val
        self.left = left

import queue
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def bottomView(self, root):
        q = queue.Queue()

        map = {}
        q.put((root, 0))
        while q.empty() != False:
            n, c = q.get()
            map[c] = n.data
            if n.left!=None:
                q.put((n.left, c-1))
            if n.right!=None:
                q.put((n.right, c+1))
        
        keys = list(map.keys())
        keys.sort()
        res = []
        for k in keys:
            res.append(k)
        return res
            

    def bottomViewMy(self,root):
        map = {}
        self.__verticalMapping(root, 0, 0, map)
        cols = list(map.keys())
        cols.sort()
        res = []

        for ci in cols:
            rows = list(map[ci].keys())
            r = max(rows)
            res.append(map[ci][r][-1])
        return res

    def __verticalMapping(self, node, row, col, map):
        if node==None:
            return
        
        if col not in map:
            map[col] = {}
        if row not in map[col]:
            map[col][row] = []
        
        map[col][row].append(node.data)

        self.__verticalMapping(node.left, row+1, col-1, map)
        self.__verticalMapping(node.right,row+1, col+1, map)