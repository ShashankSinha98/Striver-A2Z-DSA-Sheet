from TreeNode import TreeNode
from typing import Optional, List
import queue


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return
        
        q = queue.Queue()
        q.put(root)
        res = []
        currLevelNodeCount=1
        nextLevelNodeCount=0

        while q.empty()==False:
            n = q.get()
            res.append(n.val)
            currLevelNodeCount-=1
            if n.right!=None:
                q.put(n.right)
                nextLevelNodeCount+=1
            if n.left!=None:
                q.put(n.left)
                nextLevelNodeCount+=1
            
            while currLevelNodeCount!=0:
                x = q.get()
                currLevelNodeCount-=1
                if x.right!=None:
                    q.put(x.right)
                    nextLevelNodeCount+=1
                if x.left!=None:
                    q.put(x.left)
                    nextLevelNodeCount+=1
                    
            currLevelNodeCount = nextLevelNodeCount
            nextLevelNodeCount = 0
        
        return res


if __name__ == "__main__":
    s = Solution()
    r = TreeNode(1, left=TreeNode(2,left=TreeNode(4)), right=TreeNode(3))
    print(s.rightSideView(r))
        
