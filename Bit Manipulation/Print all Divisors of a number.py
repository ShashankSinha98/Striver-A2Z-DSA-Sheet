from typing import List

def printDivisors(n: int) -> List[int]:
    res1 = []
    res2 = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res1.append(i)

            if n//i != i:
                res2.append(n//i)
        i += 1
    for i in range(len(res2)-1, -1, -1):
        res1.append(res2[i])
    return res1


if __name__ == "__main__":
    n = 10
    ans = printDivisors(n)
    print(ans)
