from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    def _check(arr: List[int], idx: int, sum: int, k: int) -> bool:
        if idx == len(arr):
            return sum == k
        
        if sum+arr[idx] <= k:
            ans = _check(arr, idx+1, sum+arr[idx], k)
            if ans:
                return True
        
        return _check(arr, idx+1, sum, k)
    
    return _check(a, 0, 0, k)

if __name__ == "__main__":
    arr = [4,2,5,6,7]
    k = 14
    ans = isSubsetPresent(len(arr), k, arr)
    print(ans)