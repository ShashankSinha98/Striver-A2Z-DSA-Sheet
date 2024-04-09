from typing import List

def reverseStack(stack: List[int]) -> None:
    def _reverseStack(idx: int, stack: List[int]):
        n = len(stack)
        if idx >= n//2:
            return
        
        stack[idx], stack[n-idx-1] = stack[n-idx-1], stack[idx]
        _reverseStack(idx+1, stack)
    
    _reverseStack(0, stack)


if __name__ == "__main__":
    st = [1,2,3,4,5]
    reverseStack(st)
    print(st)