import math
def countPrimes(n: int) -> int:
    lim = int(math.ceil(math.sqrt(n)))
    res = []
    for i in range(2, lim+1):
        if n%i == 0:
            res.append(i)

            while n%i == 0:
                n = n//i
    
    if n != 1:
        res.append(n)
    
    return res


if __name__ == "__main__":
    n = 780
    ans = countPrimes(n)
    print(ans)

