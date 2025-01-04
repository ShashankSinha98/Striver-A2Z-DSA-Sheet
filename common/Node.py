from typing import Optional
# GFG

class Node:
    def __init__(self, val, left: Optional['Node']=None, right: Optional['Node']=None):
        self.right = right
        self.data = val
        self.key = val
        self.left = left