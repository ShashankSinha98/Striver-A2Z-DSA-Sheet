class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        res = []

        for qi in indices:
            c = 0
            for i in range(qi+1, N):
                if arr[i] > arr[qi]:
                    c += 1
            res.append(c)
        
        return res
    
if __name__ == "__main__":
    s = Solution()
    arr = [3,4,2,7,5,8,10,6]
    N = len(arr)
    queries = 2
    indices = [0, 5]
    print(s.count_NGEs(N, arr, queries, indices))