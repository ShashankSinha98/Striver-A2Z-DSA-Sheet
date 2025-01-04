class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        n = len(start)
        if n==0:
            return 0
        
        arr = []
        for i in range(n):
            arr.append((start[i], end[i], i))
        
        arr.sort(key=lambda x: x[1])
        
        c = 1
        finishTime = arr[0][1]
        for i in range(1, n):
            st, en, pos = arr[i]
            if finishTime < st:
                c+=1
                finishTime = en
        return c
    
if __name__ == "__main__":
    s = Solution()
    st = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    print(s.maximumMeetings(st, end))