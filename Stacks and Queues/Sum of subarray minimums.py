from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        st, left = [], []
        i = 0

        while i < len(arr):

            if len(st) == 0:
                st.append((arr[i], i))
                left.append(i)
                i+=1
            
            elif st[-1][0] >= arr[i]:
                st.pop()
            
            else:
                val = st[-1][1]
                st.append((arr[i], i))
                left.append(i-val-1)
                i+=1
        
        #print("left: ", left)

        st, right = [], []
        i = len(arr)-1

        while i >= 0:
            if len(st) == 0:
                st.append((arr[i], i))
                right.append(len(arr)-i-1)
                i-=1
            
            elif st[-1][0] > arr[i]:
                st.pop()
            
            else:
                val = st[-1][1]
                st.append((arr[i], i))
                right.append(val-i-1)
                i-=1
        
        right = right[::-1]
        
        #print("right: ", right)

        res = 0
        for i in range(len(arr)):
            res += (arr[i] * (left[i]+1) * (right[i]+1)) % (10**9+7)

        return res  % (10**9+7)


if __name__ == "__main__":
    s = Solution()
    arr = [3,1,4,2]
    print(s.sumSubarrayMins(arr))