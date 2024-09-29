from typing import Dict

class Solution:
    
    
    def insertInDict(self, myDict: Dict[str,int], ch: str):
        if ch not in myDict:
            myDict[ch] = 1
        else:
            myDict[ch] += 1
    

    def removeFromDict(self, myDict: Dict[str, int], ch: str):
        if ch not in myDict:
            return
        
        if myDict[ch] == 1:
            myDict.pop(ch)
        else:
            myDict[ch]-=1

    def longestKSubstr(self, s, k):
        cDict: Dict[str, int] = {}
        i, j = 0, -1
        maxLen = -1

        while j < len(s)-1:
            while len(cDict) > k and i <= j:
                self.removeFromDict(cDict, s[i])
                i+=1
            
            j+=1
            self.insertInDict(cDict, s[j])
            if len(cDict) == k:
                maxLen = max(maxLen, j-i+1)
        
        return maxLen


if __name__ == "__main__":
    s = Solution()
    st = "abababcccc"
    k = 2
    print(s.longestKSubstr(st, k))