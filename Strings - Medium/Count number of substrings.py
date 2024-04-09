from typing import *

def countSubStrings(s: str, k: int) -> int:
    n = len(s)
    res = 0
    for i in range(n):
        char_arr = [0] * 26
        dist_count = 0
        for j in range(i, n):
            c = s[j]

            if char_arr[ord(c)-ord('a')] == 0:
                dist_count +=1
            
            char_arr[ord(c)-ord('a')] += 1

            #print(c, char_arr, dist_count)
            
            if dist_count == k:
                res += 1
            elif dist_count > k:
                break            

    return res


if __name__ == "__main__":
    s = "aacfssa"
    k = 3
    print(countSubStrings(s, k))