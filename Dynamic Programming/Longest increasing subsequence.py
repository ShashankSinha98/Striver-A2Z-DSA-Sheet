class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        lis = [1]*N
        idxs = [0]*N
        for i in range(1, N):
            for j in range(i):
                if arr[j] < arr[i]:
                    if lis[i]<lis[j]+1:
                        lis[i] = lis[j]+1
                        idxs[i] = j 
        
        res = []
        max_idx, max_val = 0, 1
        for i in range(N):
            if lis[i]>max_val:
                max_val = lis[i]
                max_idx = i
        
        i = max_idx
        while idxs[i]!=i:
            res.append(arr[i])
            i = idxs[i]

        if len(res)==0 or arr[i]<res[-1]:
            res.append(arr[i])
        return res[::-1]


if __name__=="__main__":
    s = Solution()
    arr = [1]
    #arr = [77, 42, 22, 54, 95, 13, 72, 25, 54, 93, 22, 74, 75, 6, 90, 27, 84, 11, 6, 64, 100, 47, 20, 8, 57]
    #arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
    N = len(arr)
    print(s.longestIncreasingSubsequence(N, arr))