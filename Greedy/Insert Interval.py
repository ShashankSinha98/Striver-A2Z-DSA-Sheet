from typing import List
import sys

class Solution:
    
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [newInterval]

        for i in range(len(intervals)):
            ia, ib = intervals[i]
            la, lb = res[-1]
            if ib < la:
                tmp = res.pop()
                res.append(intervals[i])
                res.append(tmp)
            elif ia > lb:
                res.append(intervals[i:])
                return res
            else:
                st = min(ia, la)
                end = max(ib, lb)
                res[-1][0] = st
                res[-1][1] = end
        
        return res
        

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        is_overlap = False

        i, n = 0, len(intervals)
        nia, nib = newInterval

        for i in range(n):
            ia, ib = intervals[i]
            if ib < nia: # interval lie to left of new interval
                res.append(intervals[i])
            elif ia > nib: # interval lie to right of new interval
                if not is_overlap: # no overlap found, so add new interval first and all remm intervals
                    res.append(newInterval)
                    res.extend(intervals[i:])
                    return res
                else: # overlap was there, insert updated interval and all remm intervals
                    res.append([nia, nib]) # nia, nib may not be same as new interval.
                    res.extend(intervals[i:])
                    return res
            else: # overlap found
                is_overlap = True
                nia = min(nia, ia)
                nib = max(nib, ib)
                if i==n-1: # new interval overlaps/keeps overlaping until last item, add updated item in res
                    res.append([nia, nib])
        
        # no overlap found and we reached till here (newInterval not lie in between, lie in last)
        # add at last
        if not is_overlap:
            res.append(newInterval)
        return res

if __name__ == "__main__":
    s = Solution()
    intervals = [[1,2]]
    ni = [2,8]
    print(s.insert(intervals, ni))