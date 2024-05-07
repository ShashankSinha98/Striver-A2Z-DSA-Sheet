from typing import List

def subsetSum(num: List[int]) -> List[int]:
    ans = []

    def _solve(idx: int, sum: int):

        if idx == len(num):
            ans.append(sum)
            return
    
        _solve(idx+1, sum+num[idx])

        _solve(idx+1, sum)
    
    _solve(0, 0)
    ans.sort()
    return ans


if __name__ == "__main__":
    arr = [1,2,3]
    ans = subsetSum(arr)
    print(ans)