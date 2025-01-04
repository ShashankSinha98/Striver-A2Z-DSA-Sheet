from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        

        for i in range(1, len(intervals)):
            ia, ib = intervals[i]
            la, lb = res[-1]
            if ia > lb: # no overlap
                res.append(intervals[i])
            else:
                st = min(ia, la)
                end = max(ib, lb)
                res[-1][0] = st
                res[-1][1] = end
        
        return res
    
if __name__ == "__main__":
    s = Solution()
    intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    print(s.merge(intervals))