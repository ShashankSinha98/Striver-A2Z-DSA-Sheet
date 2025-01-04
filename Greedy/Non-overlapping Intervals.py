from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        overlap_count = 0
        last_pos = 0
        for i in range(1, len(intervals)):
            ai, bi = intervals[i]
            la, lb = intervals[last_pos]

            if ai < lb:
                overlap_count+=1
            else:
                last_pos = i
        
        return overlap_count

if __name__ == "__main__":
    s = Solution()
    intervals = [[1,2],[2,3]]
    print(s.eraseOverlapIntervals(intervals))
