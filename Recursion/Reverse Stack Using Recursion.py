from typing import List

def _insert_bottom(stack: List[int], n: int):

    if len(stack) == 0:
        stack.append(n)
        return

    elem = stack.pop()
    _insert_bottom(stack, n)
    stack.append(elem)

def reverseStack(stack: List[int]) -> None:
    
    if len(stack) <= 1:
        return
    
    elem = stack.pop()
    reverseStack(stack)
    _insert_bottom(stack, elem)
    
    


if __name__ == "__main__":
    st = [1,2,3,4,5]
    reverseStack(st)
    print(st)