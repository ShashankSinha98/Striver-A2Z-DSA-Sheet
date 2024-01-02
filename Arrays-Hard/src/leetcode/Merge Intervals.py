from typing import List

class Solution(object):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res: List[List[int]] = []
        
        intervals.sort(key=lambda arr: arr[0])

        for i in range(len(intervals)):

            if i < len(intervals)-1:
                a, b = intervals[i]
                c, d = intervals[i+1]

                if c > b:
                    res.append([a,b])
                elif b>=c and d>=b:
                    intervals[i+1] = [a,d]
                elif b>=c and d<b:
                    intervals[i+1] = [a,b]
                else:
                    print("*")
            else:
                a, b = intervals[i]
                res.append([a,b])
            
        return res

if __name__ == "__main__":
    s = Solution()
    intervals = [[1,4],[0,4]]
    print(s.merge(intervals))
        