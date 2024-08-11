class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        obc=0
        req=0
        for si in s:
            if si=='(':
                obc+=1
            else:
                if obc >0:
                    obc-=1
                else:
                    req+=1
        return req+obc