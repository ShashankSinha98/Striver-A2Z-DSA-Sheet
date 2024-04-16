from typing import *

def setBits(N : int) -> int:
    i = 0
    while (1<<i) <= N and (1<<i)&N != 0:
        i += 1
    
    if (1<<i) > N:
        return N
    
    return N | (1<<i)

if __name__ == "__main__":
    N = 10
    print(setBits(N))