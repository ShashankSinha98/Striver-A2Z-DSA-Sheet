import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        A.sort()
        B.sort()
        
        res = []
        i, j = len(A)-1, len(B)-1
        heap = []
        #s = set()

        heapq.heappush(heap, (-1*(A[i]+B[j]), i, j))
        #s.add((i, j))

        while len(res) < K:
            mSum, i, j = heapq.heappop(heap)
            res.append(-1*mSum)

            if i-1>=0: #and (i-1,j) not in s:
                heapq.heappush(heap, (-1*(A[i-1]+B[j]), i-1, j))
                #s.add((i-1,j))
            
            if j-1>=0: #and (i,j-1) not in s:
                heapq.heappush(heap, (-1*(A[i]+B[j-1]), i, j-1))
                #s.add((i,j-1))

        return res



if __name__ == "__main__":
    s = Solution()
    A = [1,4,2,3]
    B = [2,5,1,6]
    N = len(A)
    K = 4
    print(s.maxCombinations(N,K,A,B))