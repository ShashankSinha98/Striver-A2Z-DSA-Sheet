from typing import Optional, List
import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        
        q = queue.Queue()
        q.put(root)

        nodeCountInCurrLevel=1
        nodeCountInNextLevel=0
        res = []

        while q.empty()==False:
            tmp = []
            while nodeCountInCurrLevel!=0:
                n = q.get()
                tmp.append(n.val)
                nodeCountInCurrLevel-=1

                if n.left != None:
                    q.put(n.left)
                    nodeCountInNextLevel+=1
                
                if n.right != None:
                    q.put(n.right)
                    nodeCountInNextLevel+=1
                
            res.append(tmp.copy())
            
            nodeCountInCurrLevel = nodeCountInNextLevel
            nodeCountInNextLevel = 0
        return res
    

if __name__ == "__main__":
    s = Solution()
    n = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    res = s.levelOrder(n)
    print(res)
    
        