from typing import *

def twoOddNum(arr : List[int]) -> List[int]:
    res = 0
    for i in arr:
        res = res ^ i
    
    pos = 0
    while (res & (1<<pos)) == 0:
        pos += 1
    
    g1, g2 = 0, 0

    for ni in arr:
        if (ni & (1<<pos)) != 0:
            g1 = g1 ^ ni
        else:
            g2 = g2 ^ ni
    
    if g1 > g2:
        return [g1, g2]
    else:
        return [g2, g1]


if __name__ == "__main__":
    arr = [2,4,1,3,2,4]
    print(twoOddNum(arr))