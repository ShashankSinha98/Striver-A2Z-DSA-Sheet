from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi, si = 0, 0
        cnt = 0

        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                cnt+=1
                si+=1
                gi+=1
            else:
                si+=1
        return cnt

if __name__ =="__main__":
    so = Solution()
    g = [1,2]
    s = [1,2,3]
    print(so.findContentChildren(g,s))