from typing import List

class Solution:
    def fourSum(self, a: List[int], target: int) -> List[List[int]]:
        a.sort()
        n = len(a)
        res = []
        
        i = 0
        while i < n-3:
            if i!=0: 
                while i < n-3 and a[i]==a[i-1]:
                    i+=1
            
            j = i+1
            while j < n-2:
                if j!=i+1:
                    while j < n-2 and a[j]==a[j-1]:
                        j+=1

                k,l = j+1, n-1
                while k < l:
                    #print(f"{i}, {j}, {k}, {l}")
                    total = a[i] + a[j] + a[k] + a[l]

                    if total == target:
                        #print(f">> {i}, {j}, {k}, {l}")
                        res.append([a[i], a[j], a[k], a[l]])
                        k+=1
                        l-=1

                        while k < l and a[k] == a[k-1]:
                            k+=1  
                        while k < l and a[l] == a[l+1]:
                            l-=1

                    elif total > target:
                        l -= 1
                    
                    else:
                        k += 1

                j += 1
            i+=1

        return res


if __name__ == "__main__":
    s = Solution()
    nums = [0,0,4,-2,-3,-2,-2,-3]
    target = -1
    res = s.fourSum(nums, target)
    print(res)