from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _generate(self, n: int, obc: int, cbc: int, output: str, res: List[str]):
            if obc == 0 and cbc == 0:
                res.append(output)
                return
            
            if len(output) == 0 or obc == cbc: # always start with open bracket
                output += '('
                _generate(self, n, obc-1, cbc, output, res)
                output = output[:-1]
            
            else:
                if obc > 0: 
                    output += '('
                    _generate(self, n, obc-1, cbc, output, res)
                    output = output[:-1]
                
                if cbc > 0:
                    output += ')'
                    _generate(self, n, obc, cbc-1, output, res)
                    output = output[:-1]

        res = []
        _generate(self, n, n, n, "", res)
        return res
    

if __name__ == "__main__":
    s = Solution()
    n = 2
    res = s.generateParenthesis(n)
    print(res)