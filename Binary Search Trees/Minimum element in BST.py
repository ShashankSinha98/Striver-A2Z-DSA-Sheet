from cimports import Node
from typing import Optional

class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root: Optional[Node|None]) -> int:
        if root==None:
            return -1
        
        if root.left == None:
            return root.data
        
        return self.minValue(root.left)