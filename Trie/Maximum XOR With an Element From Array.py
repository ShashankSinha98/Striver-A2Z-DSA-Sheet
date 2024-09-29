from typing import List

class TrieNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.childrens = [None, None]

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(val=-1)
    
    def add(self, num: int) -> None:
        tmp = self.root
        repr = ""
        for i in range(31, -1, -1):
            bit = 1 if((1<<i)&num)>0 else 0
            if tmp.childrens[bit]==None:
                nn = TrieNode(val=bit)
                tmp.childrens[bit]=nn
            repr += f"{bit}"
            tmp = tmp.childrens[bit]

    def print(self):
        tmp = self.root
        queue = [tmp]
        pos = 31
        while len(queue) != 0:
            n = len(queue)
            while n!= 0:
                item = queue.pop(0)
                leftchild = item.childrens[0]
                rightchild = item.childrens[1]
                print(f"pos: {pos}, lc: {leftchild!=None}, rc: {rightchild!=None}")
                if leftchild != None:
                    queue.append(leftchild)
                if rightchild != None:
                   queue.append(rightchild)
                
                n-=1
            
            pos-=1
    
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


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = [None] * len(queries)
        tr = Trie()
        nums.sort()
        
        idx_queries = []
        for i in range(len(queries)):
            xi = queries[i][0]
            mi = queries[i][1]
            idx_queries.append((i, xi, mi))

        sorted_list = sorted(idx_queries, key=lambda qi: qi[2])

        ni = 0
        for i in range(len(sorted_list)):
            xi = sorted_list[i][1]
            mi = sorted_list[i][2]
            max_xor = -1
            while ni < len(nums) and nums[ni] <= mi:
                tr.add(nums[ni])
                ni+=1
            
            if ni != 0:
                max_xor = tr.maxXor(xi)
            
            res[sorted_list[i][0]] = max_xor

        return res

if __name__ == "__main__":
    s = Solution()
    nums = [536870912,0,534710168,330218644,142254206]
    queries = [[558240772,1000000000],[307628050,1000000000],[3319300,1000000000],[2751604,683297522],[214004,404207941]]
    print(s.maximizeXor(nums, queries))