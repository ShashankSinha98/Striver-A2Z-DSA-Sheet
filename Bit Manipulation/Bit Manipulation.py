from typing import *

def bitManipulation(num : int, i : int) -> List[int]:
    # Write your code here.
    a = 1 if (num & (1 << (i-1)) > 0) else 0
    b = num | (1 << (i-1))
    c = num & (~(1 << (i-1)))
    return [a, b, c]

if __name__ == "__main__":
    num = 11
    i= 2
    print(bitManipulation(num, i))