class TrieNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.childrens = [None, None]

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(val = -1)
    
    def add(self, num: int) -> None:
        tmp = self.root
        for i in range(31, -1, -1):
            bit = 1 if ((num & (1<<i)) > 0 ) else 0
            
            if tmp.childrens[bit] == None:
                nn = TrieNode(bit)
                tmp.childrens[bit] = nn
            
            tmp = tmp.childrens[bit]
    
    def maxXor(self, num: int) -> int:
        value = 0
        tmp = self.root

        for i in range(31, -1, -1):
            bit = 1 if ((num & (1<<i)) > 0 ) else 0
            rev_bit = 1 if bit==0 else 0
            #print(f"bit pos: {i}, bit val: {bit}")

            if tmp.childrens[rev_bit] != None:
                #print(f"rev bit found for bit pos: {i}")
                value += (1<<i)
                tmp = tmp.childrens[rev_bit]
            else:
                tmp = tmp.childrens[bit]
        
        return value

from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        tr = Trie()
        for ai in nums:
            tr.add(num= ai)
        
        max_xor = 0
        for ai in nums:
            max_poss_xor = tr.maxXor(num= ai)
            max_xor = max(max_xor, max_poss_xor)
        
        return max_xor


if __name__ == "__main__":
    s = Solution()
    arr = [14,70,53,83,49,91,36,80,92,51,66,70]
    ans = s.findMaximumXOR(nums=arr)
    print(ans)
        

