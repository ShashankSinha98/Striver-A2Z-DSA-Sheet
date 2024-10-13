from TreeNode import TreeNode
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        pMap = {}
        self.__buildParentMap(root, pMap)
        visited = set()
        dist = 0
        q = [target]

        while len(q)!=0 and dist!=k:
            tmp = []
            while len(q)!=0:
                n = q.pop(0)
                visited.add(n)
                if n.left!=None and n.left not in visited:
                    tmp.append(n.left)
                
                if n.right!=None and n.right not in visited:
                    tmp.append(n.right)
                
                if n in pMap and pMap[n] not in visited:
                    tmp.append(pMap[n])
            
            if len(tmp)!=0: 
                dist+=1
            
            q.extend(tmp)
        return [qi.val for qi in q]



    def __buildParentMap(self, root: TreeNode, pMap: dict[TreeNode, TreeNode]):
        if root==None:
            return
        
        q = [root]
        while len(q)!=0:
            n = q.pop()
            if n.left!=None:
                pMap[n.left]=n
                q.append(n.left)
            
            if n.right!=None:
                pMap[n.right]=n
                q.append(n.right)


if __name__ == "__main__":
    s = Solution()
    t = TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4)))
    r1 = TreeNode(3, left=t, right=TreeNode(1, left=TreeNode(0), right=TreeNode(8)))
    print(s.distanceK(r1, t, k=0))