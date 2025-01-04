from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def __is_pred(w1: str, w2: str): # w2 > w1 always
            l1, l2 = len(w1), len(w2)

            if l2-l1 != 1:
                return False
            
            i, j, diff = 0, 0, 0
            while i<l1 and j<l2:
                if w1[i]==w2[j]:
                    i+=1
                    j+=1
                else:
                    diff+=1
                    j+=1
            
            return True if((i==l1 and diff==0) or (diff==1)) else False
        
        n = len(words)
        if n<=1:
            return n
        
        words.sort(key =lambda x: len(x))
        lsc = [1]*n
        
        max_val = 1
        for i in range(1, n):
            for j in range(i):
                if __is_pred(words[j], words[i]) and lsc[j]+1>lsc[i]:
                    lsc[i] = lsc[j]+1
                    max_val = max(max_val, lsc[i])
        
        return max_val
    

if __name__ == "__main__":
    s = Solution()
    #words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    words= ["a","b","ba","bca","bda","bdca"]
    print(s.longestStrChain(words))