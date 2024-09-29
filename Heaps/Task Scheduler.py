from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cfreq = [0]*26
        for i in tasks:
            cfreq[ord(i)-ord('A')]+=1
        
        heap = []
        for i in cfreq:
            if i>0:
                heapq.heappush(heap, i*-1)
        
        q = []
        t = 0
        while len(heap)!=0 or len(q)!=0:
            t+=1
            if len(q)>0 and (q[0][1]==t or len(heap)==0):
                tmp = q.pop(0)
                if len(heap)==0:
                    t = tmp[1]
                heapq.heappush(heap, tmp[0])
            
            x = heapq.heappop(heap)
            x+=1
            if x!=0:
                q.append((x, t+n+1))
        
        return t

                
if __name__ == "__main__":
    s = Solution()
    tasks = ["A","A","A", "B","B","B"]
    n = 3

    ans = s.leastInterval(tasks, n)
    print(ans)
        