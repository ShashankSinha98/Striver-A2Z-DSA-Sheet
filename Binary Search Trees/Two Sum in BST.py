from typing import Optional
from cimports import TreeNode

import sys

class Solution:
    def __init__(self, root: Optional[TreeNode]=None):
        self.nextSt = []
        tmp = root
        while tmp != None:
            self.nextSt.append(tmp)
            tmp = tmp.left
        
        self.prevSt = []
        tmp = root
        while tmp != None:
            self.prevSt.append(tmp)
            tmp = tmp.right

    def __next(self) -> Optional[TreeNode]:
        if len(self.nextSt)==0:
            return None
        
        res = self.nextSt.pop()
        if res.right!=None:
            tmp = res.right
            
            while tmp != None:
                self.nextSt.append(tmp)
                tmp = tmp.left
        
        return res
    
    def __prev(self) -> Optional[TreeNode]:
        if len(self.prevSt)==0:
            return None
        
        res = self.prevSt.pop()
        if res.left!=None:
            tmp = res.left
            
            while tmp != None:
                self.prevSt.append(tmp)
                tmp = tmp.right
        
        return res

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.__init__(root)
        left = self.__next()
        right = self.__prev()

        while left!=None and right!=None and left.val < right.val:
            total = left.val + right.val
            
            if total == k:
                return True
            elif total > k:
                right = self.__prev()
            else:
                left = self.__next()
        
        return False


if __name__ == "__main__":
    s = Solution()
    r = TreeNode(5, left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)), right=TreeNode(6, right=TreeNode(7)))
    print(s.findTarget(r, 10))
        

        