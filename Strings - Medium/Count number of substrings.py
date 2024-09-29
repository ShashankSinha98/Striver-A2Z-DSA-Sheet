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

#  Optimized approach
class Solution:
    def substrCountForKIsOne(self, s):
        cdict = {}
        end = -1
        st = 0
        ans = 0
        while True:
            f1, f2 = False, False
            # expand
            while end < len(s)-1:
                f1 = True
                end+=1
                self.putInDict(cdict, s[end])

                if len(cdict)==2:
                    self.removeFromDict(cdict, s[end])
                    end-=1
                    break
            
            # shrink
            while st <= end:
                f2 = True
                if len(cdict) == 1:
                    ans += (end-st+1)
                
                self.removeFromDict(cdict, s[st])
                st+=1

                if len(cdict) == 0:
                    break
            
            if f1==False and f2==False:
                break

        return ans



    def substrCount (self,s, k):
        dicts = {}
        dictb = {}
        ends, endb = -1, -1
        st = 0
        ans = 0

        if k==1:
            return self.substrCountForKIsOne(s)
        
        while True:
            f1, f2, f3 = False, False, False

            # make big valid
            while endb < len(s)-1:
                f1 = True
                endb += 1
                self.putInDict(dictb, s[endb])

                if len(dictb) == k+1:
                    self.removeFromDict(dictb, s[endb])
                    endb-=1
                    break
            
            # make small valid
            while ends < endb:
                f2 = True
                ends+=1
                self.putInDict(dicts, s[ends])

                if len(dicts) == k:
                    self.removeFromDict(dicts, s[ends])
                    ends-=1
                    break
            
            # shrink
            while st <= ends:
                f3 = True
                if len(dictb) == k and len(dicts) == k-1:
                    ans += ((endb-st+1) - (ends-st+1))
                
                self.removeFromDict(dicts, s[st])
                self.removeFromDict(dictb, s[st])
                st+=1

                if len(dictb) < k or len(dicts) < k-1:
                    break
            
            if f1==False and f2==False and f3==False:
                break
        
        return ans


    def putInDict(self, dict, item):
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] = dict[item] + 1
    
    def removeFromDict(self, dict, item):
        if dict[item] == 1:
            dict.pop(item)
        else:
            dict[item] = dict[item] - 1

if __name__ == "__main__":
    s = "abaaca"
    k = 1
    sol = Solution()
    ans = sol.substrCount(s, k)
    print(ans)
