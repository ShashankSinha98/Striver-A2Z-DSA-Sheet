from typing import *

def findXOR(L : int, R : int) -> int:
    
    if L == 0:
        return xorFrom1ToN(R)
    
    a = xorFrom1ToN(L-1)
    b = xorFrom1ToN(R)

    return a ^ b


def xorFrom1ToN(n: int) -> int:
    if n%4 == 1:
        return 1
    elif n%4==3:
        return 0
    elif n%4==2:
        return n+1
    else:
        return n
    
if __name__ == "__main__":
    ans = findXOR(3, 5) 
    print(ans)