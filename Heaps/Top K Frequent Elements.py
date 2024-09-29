from typing import List
import heapq

class Solution:

    # using arr sort
    def topKFrequentArray(self, nums: List[int], k: int) -> List[int]:
        n_map = {}
        for i in nums:
            if i not in n_map:
                n_map[i] = 0
            n_map[i]+=1
        
        arr = []
        for ki in n_map.keys():
            arr.append((ki, n_map[ki]))
        
        
        arr = sorted(arr, key=lambda a: a[1], reverse=True)
        res = []
        
        for i in range(k):
            if i >= len(arr):
                break
            res.append(arr[i][0])
        
        return res
        
    # Using heap
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        n_map = {}
        for i in nums:
            if i not in n_map:
                n_map[i] = 0
            n_map[i]+=1
        
        hArr = []
        for ki in n_map.keys():
            hArr.append((-1*n_map[ki], ki))
        
        heapq.heapify(hArr)
        res = []
        while len(res) < k:
            c, ki = heapq.heappop(hArr)
            res.append(ki)
        
        return res
    
    # using buckets
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_map = {}
        for i in nums:
            if i not in n_map:
                n_map[i] = 0
            n_map[i]+=1
        
        bucket = [None]*len(nums)
        
        for ki in n_map.keys():
            c = n_map[ki]
            if bucket[c]==None:
                bucket[c] = []
            bucket[c].append(ki)
        
        res = []
        i = len(nums)-1
        while i>=0 and len(res)<k:
            ibucket = bucket[i]
            if ibucket!= None:
                while len(res)<k and len(ibucket)>0:
                    tmp = ibucket.pop()
                    res.append(tmp)
            i-=1
        
        return res


if __name__ == "__main__":
    s = Solution()
    arr = [2,2,1,1,1,3]
    k = 2
    print(s.topKFrequent(arr,k))
