import sys

def kthElement(arr1: list[int], len1: int, arr2: list[int], len2: int, k: int) -> int:
    low = max(0, k-len2)
    high = min(k, len1)

    while low <= high:
        cut1 = (low+high) // 2
        cut2 = k - cut1

        l1 = arr1[cut1-1] if cut1-1 >=0 else -sys.maxsize
        l2 = arr2[cut2-1] if cut2-1 >=0 else -sys.maxsize

        r1 = arr1[cut1] if cut1 < len1 else sys.maxsize
        r2 = arr2[cut2] if cut2 < len2 else sys.maxsize

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return 0.0


if __name__ == "__main__":
    arr1 = [1,2,3,5,6]
    arr2 = [4,7,8,9,100]
    k = 6

    ans = kthElement(arr1, len(arr1), arr2, len(arr2), k)
    print(ans)