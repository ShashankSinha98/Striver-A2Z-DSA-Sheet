# def countUniqueSubsequences(s: str) -> int:
    
#     def  _cus(s: str, idx: int, map: dict) -> int:
        
#         if idx == len(s):
#             return 1
        
#         c = s[idx]

#         if c not in map:
#             map[c] = idx
#             return 2 * _cus(s, idx+1, map)
#         else:
#             val = map[c]
#             return 2 * _cus(s,  idx+1, map) 
    
#     map = {}
#     ans = 0
#     return _cus(s, 0, map)

def countUniqueSubsequences(s: str) -> int:

    map = {}
    ans = 1
    for i  in range(len(s)):
        c = s[i]
        if c not in map:
            map[c] = ans
            ans *= 2
        else:
            val = map[c]
            map[c] = ans
            ans = (ans*2) - (val)
            

    return ans


def moreSubsequence(n: int, m: int, a: str, b:str) -> str:
    return a if countUniqueSubsequences(a) >= countUniqueSubsequences(b) else b

if __name__ == "__main__":
    a = "abc"
    b = "dddd"
    print(moreSubsequence(0,0, a, b))
    print(countUniqueSubsequences(b))