import sys

class Solution:
    def minWindow(self, s1, s2):
        min_len, st_idx = sys.maxsize, -1
        l, r, k = 0, 0, 0

        while r < len(s1):

            if s1[r] == s2[k]:
                if k != len(s2)-1:
                    k+=1
                    r+=1
                else:
                    # reverse
                    l = r
                    nxt_st_idx = -1
                    while k>=0:
                        if k > 0 and s1[l] == s2[0]:
                            nxt_st_idx = l
                            
                        if s1[l]==s2[k]:
                            k-=1
                        l-=1
                    
                    k+=1
                    l+=1

                    if r-l+1 < min_len:
                        min_len = r-l+1
                        st_idx = l
                    
                    if nxt_st_idx != -1:
                        l = r = nxt_st_idx
                    else:
                        r = r+1
                        l = r
            else:
                r+=1

        return "" if st_idx == -1 else s1[st_idx:st_idx+min_len]


if __name__ == "__main__":
    s = Solution()
    s1 = "dgfbkfibbkihjkaediegihhdjfaaedhdffaedcehhagedfjg"
    s2 = "dgjhfh"
    print(s.minWindow(s1, s2))
