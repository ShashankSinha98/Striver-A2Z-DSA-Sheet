from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        curr = []

        def _isPalindrome(myStr) -> bool:
            return myStr == myStr[::-1]
        
        def _solve(ss):

            if len(ss) == 0:
                res.append(curr[:])
                return
        
            for i in range(len(ss)):
                tmp = ss[:i+1]

                if _isPalindrome(tmp):
                    curr.append(tmp)
                    _solve(ss[i+1:])
                    curr.pop()

        _solve(s)

        return res


if __name__ == "__main__":
    s = Solution()
    str = "aabb"
    print(s.partition(str))