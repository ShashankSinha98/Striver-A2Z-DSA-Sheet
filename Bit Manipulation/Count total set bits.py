def countSetBits(N: int) -> int:
    if N==0 or N==1:
        return N

    x = 0
    while (1 << x) <= N:
        x+=1
    x = x-1
    
    return ((1<<x-1)*x) + (N-(1<<x)+1) + countSetBits(N-(1<<x))

if __name__ == "__main__":
    ans = countSetBits(20)
    print(ans)