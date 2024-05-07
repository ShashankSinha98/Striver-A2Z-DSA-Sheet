from typing import List

def generateString(N: int) -> List[str]:
    
    def _gen_str(N: int, output: str, res: list):

        if N == 0:
            res.append(output)
            return
        
        if len(output) == 0 or output[-1] == '0':
            output += '0'
            _gen_str(N-1, output, res)
            output = output[:-1]
            
            output += '1'
            _gen_str(N-1, output, res)
            output = output[:-1]
        else:
            output += '0'
            _gen_str(N-1, output, res)
            output = output[:-1]
        
    
    res = []
    _gen_str(N, "", res)
    return res


if __name__ == "__main__":
    N = 2
    print(generateString(N))