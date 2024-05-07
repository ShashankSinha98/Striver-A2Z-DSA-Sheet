
def subarraysWithSumK( a:list, k:int) ->list[list]:
    def _solve(arr, curr, sum, res, k, idx):

        # if idx == len(arr):
        #     # if sum == k:
        #     #     res.append(curr.copy())
        #     return
        
        if sum > k:
            while sum > k and len(curr) != 0:
                sum -= curr[0]
                curr = curr[1:]
        
        if sum == k:
            res.append(curr.copy())
        
        if idx == len(arr):
            # if sum == k:
            #     res.append(curr.copy())
            return

        curr.append(arr[idx])
        sum += arr[idx]
        _solve(arr, curr, sum, res, k, idx+1)
        curr.pop()
        sum -= arr[idx]
    
    res = []
    _solve(a, [], 0, res, k, 0)
    return res

if __name__ == "__main__":
    arr = [9, 5, 6, 5, 5]
    k = 16
    ans = subarraysWithSumK(arr, k)
    print(ans)