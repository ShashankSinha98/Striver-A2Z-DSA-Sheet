import math


def minimiseMaxDistance(arr: [int], k: int) -> float:
    n, left, right = len(arr), 0, -1
    for i in range(n-1):
        right = max(right, arr[i+1]-arr[i])

    ans = right
    while right - left > pow(10, -6):
        gap_lim = (left + right) / 2.0
        is_poss = _is_possible(arr, k, gap_lim)
        # print(gap_lim, is_poss)
        if is_poss:
            ans = min(gap_lim, ans)
            right = gap_lim
        else:
            left = gap_lim
    
    return ans



def _is_possible(arr, k, gap_lim):
    count = 0
    for i in range(len(arr)-1):
        dist = arr[i+1] - arr[i]
        div = math.floor(dist/gap_lim)
        count += (div if (dist % gap_lim)!=0 else div-1)

        if count > k:
            return False

    return True 


if __name__ == "__main__":
    arr = [1,5,8,10]
    k = 5
    print(minimiseMaxDistance(arr, k))